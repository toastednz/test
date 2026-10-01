"""Exp 1: what does ESM-2 know about the 20 amino acids?  Probe the token embedding
(and context-averaged embeddings) against physicochemistry, BLOSUM62, and the genetic code."""
import sys, json, numpy as np, torch
sys.path.insert(0,'.'); from protlib import *
from scipy.stats import spearmanr, pearsonr
from sklearn.linear_model import RidgeCV
from sklearn.model_selection import LeaveOneOut, cross_val_predict
from sklearn.decomposition import PCA
import statsmodels.api as sm

MODEL=sys.argv[1] if len(sys.argv)>1 else "facebook/esm2_t12_35M_UR50D"
tok,m=load_esm(MODEL)
ids=[tok.convert_tokens_to_ids(a) for a in AAS]
E_in=m.embeddings.word_embeddings.weight[ids].detach().numpy()

# context-averaged embeddings per residue type, several layers
seqs=read_fasta("../data/seqs/human_sp_80_250.fasta",150)+read_fasta("../data/seqs/ecoli_sp_80_250.fasta",150)
L=m.config.num_hidden_layers
sums={l:np.zeros((20,m.config.hidden_size)) for l in range(L+1)}; cnt=np.zeros(20)
with torch.no_grad():
    for s in seqs:
        out=m(**tok(s,return_tensors="pt"),output_hidden_states=True)
        idx=np.array([AAS.index(c) for c in s])
        for l in range(L+1):
            h=out.hidden_states[l][0,1:-1].numpy()
            np.add.at(sums[l],idx,h)
        np.add.at(cnt,idx,1)
E_ctx={l:sums[l]/cnt[:,None] for l in sums}

def cos(E):
    En=E/np.linalg.norm(E,axis=1,keepdims=True); return En@En.T
iu=np.triu_indices(20,1)
B=blosum62(); R=snv_reachability(); Rs=(R+R.T)/2
res={}
print(f"== {MODEL}: embedding similarity vs BLOSUM62 (Spearman over 190 pairs) ==")
for name,E in [("input_embedding",E_in)]+[(f"ctx_layer{l}",E_ctx[l]) for l in range(0,L+1,max(1,L//6))]:
    C=cos(E)[iu]
    rb=spearmanr(C,B[iu]).correlation
    rr=spearmanr(C,Rs[iu]).correlation
    # partial: SNV reachability after controlling for BLOSUM
    X=sm.add_constant(np.c_[B[iu],Rs[iu]]); fit=sm.OLS((C-C.mean())/C.std(),X).fit()
    print(f"{name:18s} rho(BLOSUM62)={rb:+.3f}  rho(SNV-reach)={rr:+.3f}  | OLS std-coef: BLOSUM {fit.params[1]:+.3f} (p={fit.pvalues[1]:.1e}), SNV {fit.params[2]:+.3f} (p={fit.pvalues[2]:.1e})")
    res[name]=dict(rho_blosum=rb,rho_snv=rr,snv_partial_p=float(fit.pvalues[2]),snv_partial_coef=float(fit.params[2]))

print("\n== leave-one-out ridge probes: embedding -> property (LOO Pearson r; n=20) ==")
def loo_r(E,y):
    model=RidgeCV(alphas=np.logspace(-2,4,25))
    pred=cross_val_predict(model,E,y,cv=LeaveOneOut())
    return pearsonr(pred,y)[0]
hdr="%-20s"%"property"+"".join("%12s"%n for n in ["input","ctx_L0","ctx_mid","ctx_last"])
print(hdr)
mid=L//2
probe={}
for pname,tab in PROPS.items():
    y=np.array([tab[a] for a in AAS],float)
    row=[loo_r(E,y) for E in (E_in,E_ctx[0],E_ctx[mid],E_ctx[L])]
    probe[pname]=row
    print("%-20s"%pname+"".join("%12.2f"%r for r in row))
# frequency confound
freq=cnt/cnt.sum()
print("%-20s"%"log_frequency"+"".join("%12.2f"%loo_r(E,np.log(freq)) for E in (E_in,E_ctx[0],E_ctx[mid],E_ctx[L])))

print("\n== PCA of input embedding: which properties align with the top PCs? ==")
pca=PCA(5).fit(E_in); Z=pca.transform(E_in)
print("explained var:",np.round(pca.explained_variance_ratio_,3))
for k in range(3):
    best=sorted(((abs(pearsonr(Z[:,k],[t[a] for a in AAS])[0]),n) for n,t in PROPS.items()),reverse=True)[:3]
    print(f"PC{k+1}: "+", ".join(f"{n} |r|={r:.2f}" for r,n in best))
print("PC1 order:", "".join(np.array(list(AAS))[np.argsort(Z[:,0])]))
print("PC2 order:", "".join(np.array(list(AAS))[np.argsort(Z[:,1])]))

json.dump(dict(model=MODEL,blosum=res,probe=probe,pc_order=["".join(np.array(list(AAS))[np.argsort(Z[:,k])]) for k in range(2)],
               Z=Z[:,:2].tolist(), expl=pca.explained_variance_ratio_.tolist()),open(f"../results/exp1_{MODEL.split('/')[-1]}.json","w"),indent=1)
