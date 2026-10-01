"""Exp 3: attention heads as unsupervised contact predictors (18 PDB proteins)."""
import sys, json, glob, numpy as np, torch
sys.path.insert(0,'.'); from protlib import *
from sklearn.linear_model import LogisticRegression
torch.set_num_threads(1)
MODEL=sys.argv[1] if len(sys.argv)>1 else "facebook/esm2_t12_35M_UR50D"
tok,m=load_esm(MODEL); L=m.config.num_hidden_layers; H=m.config.num_attention_heads
pdbs=[p for p in sorted(glob.glob("../data/pdb/*.pdb")) if not any(x in p for x in ["1LMB","1PIN"])]
MINSEP=6
data=[]
with torch.no_grad():
    for p in pdbs:
        d=load_pdb(p); s=d["seq"]; n=len(s)
        C,_=contact_map(d["cb"])
        out=m(**tok(s,return_tensors="pt"),output_attentions=True)
        A=np.stack([out.attentions[l][0,:,1:-1,1:-1].numpy() for l in range(L)]).reshape(L*H,n,n)
        A=A+A.transpose(0,2,1)
        iu=np.array([(i,j) for i in range(n) for j in range(i+MINSEP,n)])
        feats=A[:,iu[:,0],iu[:,1]].T  # pairs x heads
        y=C[iu[:,0],iu[:,1]]
        data.append(dict(name=p.split("/")[-1][:4],n=n,feats=feats,y=y))
def prec_at_L(score,y,n,frac=1.0):
    k=max(1,int(n*frac)); top=np.argsort(-score)[:k]; return y[top].mean()
# per-head precision@L averaged over proteins
PH=np.array([[prec_at_L(d["feats"][:,h],d["y"],d["n"]) for h in range(L*H)] for d in data])  # prot x heads
base=np.mean([d["y"].mean() for d in data])
mean_ph=PH.mean(0); order=np.argsort(-mean_ph)
print(f"== {MODEL}: single attention heads as contact predictors (|i-j|>={MINSEP}, Cb<8A) ==")
print(f"random baseline precision = contact density = {base:.3f}")
for h in order[:8]:
    print(f"L{h//H:2d}H{h%H:2d}: mean P@L={mean_ph[h]:.3f}  (per-protein min {PH[:,h].min():.2f} max {PH[:,h].max():.2f})")
print(f"median head P@L={np.median(mean_ph):.3f}; heads with P@L>2x baseline: {(mean_ph>2*base).sum()}/{L*H}")
# leave-one-protein-out logistic regression on all heads
res=[]
for i,d in enumerate(data):
    Xtr=np.concatenate([e["feats"] for j,e in enumerate(data) if j!=i]); ytr=np.concatenate([e["y"] for j,e in enumerate(data) if j!=i])
    clf=LogisticRegression(max_iter=3000,C=0.1).fit(Xtr,ytr)
    sc=clf.decision_function(d["feats"])
    res.append(dict(name=d["name"],n=d["n"],pL=prec_at_L(sc,d["y"],d["n"]),pL5=prec_at_L(sc,d["y"],d["n"],0.2),best_single=PH[i].max(),density=d["y"].mean()))
print("\nleave-one-protein-out logistic regression over all heads:")
for r in res: print(f"  {r['name']} n={r['n']:3d} P@L={r['pL']:.2f} P@L/5={r['pL5']:.2f} (best single head {r['best_single']:.2f}, density {r['density']:.2f})")
print(f"mean P@L={np.mean([r['pL'] for r in res]):.3f}, mean P@L/5={np.mean([r['pL5'] for r in res]):.3f}, baseline {base:.3f}")
json.dump(dict(model=MODEL,head_pL=mean_ph.tolist(),baseline=base,loo=res,top_heads=[int(h) for h in order[:10]]),open(f"../results/exp3_{MODEL.split('/')[-1]}.json","w"))
