"""Exp 2: do attention heads encode secondary-structure geometry?  (a) mean attention vs relative
offset for every head over 300 sequences; (b) on PDB proteins with DSSP, test whether i->i+3/i+4
attention is specific to helices and i->i+2 to strands."""
import sys, json, glob, numpy as np, torch
sys.path.insert(0,'.'); from protlib import *
from sklearn.metrics import roc_auc_score
torch.set_num_threads(2)
MODEL=sys.argv[1] if len(sys.argv)>1 else "facebook/esm2_t12_35M_UR50D"
tok,m=load_esm(MODEL); L=m.config.num_hidden_layers; H=m.config.num_attention_heads
D=16
seqs=read_fasta("../data/seqs/human_sp_80_250.fasta",150)+read_fasta("../data/seqs/ecoli_sp_80_250.fasta",150)
prof=np.zeros((L,H,2*D+1)); nprof=np.zeros(2*D+1)
with torch.no_grad():
    for s in seqs:
        out=m(**tok(s,return_tensors="pt"),output_attentions=True)
        n=len(s)
        for l in range(L):
            A=out.attentions[l][0,:,1:-1,1:-1].numpy()  # H,n,n
            for k,d in enumerate(range(-D,D+1)):
                if d>=0: v=A[:,np.arange(n-d),np.arange(n-d)+d]
                else:    v=A[:,np.arange(-d,n),np.arange(-d,n)+d]
                prof[l,:,k]+=v.sum(1)
        for k,d in enumerate(range(-D,D+1)): nprof[k]+=n-abs(d)
prof/=nprof
offs=np.arange(-D,D+1)
# characterize heads: for each head, the offset with max attention (excluding 0) and its share
print(f"== {MODEL}: heads whose attention is concentrated at a specific relative offset ==")
rows=[]
for l in range(L):
    for h in range(H):
        p=prof[l,h].copy(); p[D]=0
        k=np.argmax(p); share=p[k]/p.sum()
        rows.append((share,l,h,offs[k],p[k]))
rows.sort(reverse=True)
for share,l,h,d,v in rows[:25]:
    print(f"L{l:2d}H{h:2d}: peak offset {d:+3d}  mean attn {v:.3f}  share of ±{D} window {share:.2f}")
# aggregate: total attention mass at each |offset| summed over all heads, to see 'preferred' separations
agg=prof.sum((0,1)); print("\nall-head mean attention by offset (|d|=1..8):", {int(d):round(float((prof[:,:,D+d].sum()+prof[:,:,D-d].sum())/2),3) for d in range(1,9)})

# (b) DSSP test on PDB proteins
pdbs=[p for p in sorted(glob.glob("../data/pdb/*.pdb")) if not any(x in p for x in ["1LMB","1PIN"])]
att_d={d:[] for d in (1,2,3,4,5)}  # list of (L,H) arrays per residue
ss_all=[]; 
with torch.no_grad():
    for p in pdbs:
        d=load_pdb(p); ss=dssp_ss(d["bb"]); s=d["seq"]; n=len(s)
        out=m(**tok(s,return_tensors="pt"),output_attentions=True)
        A=np.stack([out.attentions[l][0,:,1:-1,1:-1].numpy() for l in range(L)])  # L,H,n,n
        for dd in att_d:
            # symmetric: attention i->i+dd plus i+dd->i
            v=A[:,:,np.arange(n-dd),np.arange(n-dd)+dd]+A[:,:,np.arange(n-dd)+dd,np.arange(n-dd)]
            att_d[dd].append(v)  # L,H,n-dd
        ss_all.append(ss)
def labels(dd, kind):
    y=[]
    for ss in ss_all:
        n=len(ss); y.append(np.array([(ss[i]==kind and ss[i+dd]==kind) for i in range(n-dd)]))
    return np.concatenate(y)
print("\n== Which heads' i->i+d attention discriminates helix (d=3,4) or strand (d=2) pairs? (AUC, 18 proteins) ==")
best={}
for dd,kind in [(4,"H"),(3,"H"),(2,"E"),(1,"H"),(1,"E"),(2,"H"),(4,"E")]:
    X=np.concatenate(att_d[dd],axis=2); y=labels(dd,kind)
    auc=np.array([[roc_auc_score(y,X[l,h]) for h in range(H)] for l in range(L)])
    l,h=np.unravel_index(auc.argmax(),auc.shape)
    lo,ho=np.unravel_index(auc.argmin(),auc.shape)
    best[f"d{dd}_{kind}"]=dict(best_head=[int(l),int(h)],auc=float(auc.max()),min_auc=float(auc.min()),min_head=[int(lo),int(ho)],n_pairs=int(len(y)),pos_rate=float(y.mean()))
    print(f"d={dd} {kind}: best L{l}H{h} AUC={auc.max():.3f}   (most anti: L{lo}H{ho} AUC={auc.min():.3f})   n={len(y)} pos={y.mean():.2f}")
# simple combined probe: logistic regression on all heads' (d=3,d=4) attention -> helix, leave-one-protein-out
from sklearn.linear_model import LogisticRegression
Xs=[];ys=[]
for i in range(len(pdbs)):
    n=len(ss_all[i]); 
    x=np.concatenate([att_d[3][i][:,:,:n-4].reshape(L*H,-1),att_d[4][i].reshape(L*H,-1)],0).T
    y=np.array([ss_all[i][j]=="H" for j in range(n-4)])
    Xs.append(x);ys.append(y)
aucs=[]
for i in range(len(pdbs)):
    Xtr=np.concatenate([Xs[j] for j in range(len(pdbs)) if j!=i]); ytr=np.concatenate([ys[j] for j in range(len(pdbs)) if j!=i])
    if ys[i].sum()==0 or ys[i].sum()==len(ys[i]): continue
    clf=LogisticRegression(max_iter=2000,C=1.0).fit(np.log(Xtr+1e-6),ytr)
    aucs.append(roc_auc_score(ys[i],clf.decision_function(np.log(Xs[i]+1e-6))))
print(f"\nLeave-one-protein-out helix classifier from (d=3,4) attention of all heads: mean AUC={np.mean(aucs):.3f} over {len(aucs)} proteins")
json.dump(dict(model=MODEL,offsets=offs.tolist(),profile=prof.tolist(),top_heads=[(float(a),int(b),int(c),int(d),float(e)) for a,b,c,d,e in rows[:40]],dssp=best,loo_helix_auc=float(np.mean(aucs))),open(f"../results/exp2_{MODEL.split('/')[-1]}.json","w"))
