"""Exp 4: masked-marginal entropy vs burial (RSA) & secondary structure.
   Exp 5: the model's substitution distribution vs BLOSUM62, physicochemistry and the genetic code,
          with a random-genetic-code permutation null."""
import sys, json, glob, numpy as np, torch
sys.path.insert(0,'.'); from protlib import *
from scipy.stats import spearmanr, pearsonr
import statsmodels.api as sm
torch.set_num_threads(int(__import__("os").environ.get("TORCH_THREADS","1")))
MODEL=sys.argv[1] if len(sys.argv)>1 else "facebook/esm2_t12_35M_UR50D"
NSEQ=int(sys.argv[2]) if len(sys.argv)>2 else 100
tok,m=load_esm(MODEL,mlm=True); aa_ids=torch.tensor([tok.convert_tokens_to_ids(a) for a in AAS]); mask_id=tok.mask_token_id
def masked_marginals(s, bs=64):
    enc=tok(s,return_tensors="pt")["input_ids"][0]; n=len(s); P=np.zeros((n,20))
    with torch.no_grad():
        for st in range(0,n,bs):
            idx=list(range(st,min(n,st+bs))); X=enc.repeat(len(idx),1)
            for r,i in enumerate(idx): X[r,i+1]=mask_id
            logits=m(input_ids=X).logits[torch.arange(len(idx)),torch.tensor(idx)+1][:,aa_ids]
            P[idx]=torch.softmax(logits,-1).numpy()
    return P
# ---- Exp 4 ----
pdbs=[p for p in sorted(glob.glob("../data/pdb/*.pdb")) if not any(x in p for x in ["1LMB","1PIN"])]
ent_all=[];rsa_all=[];ss_all=[];rho=[]
for p in pdbs:
    d=load_pdb(p); P=masked_marginals(d["seq"]); ent=-(P*np.log(P+1e-12)).sum(1); ss=dssp_ss(d["bb"])
    r=spearmanr(ent,d["rsa"]).correlation; rho.append(r); ent_all+=list(ent); rsa_all+=list(d["rsa"]); ss_all+=list(ss)
    print(f"{p.split('/')[-1][:4]}: Spearman(entropy, RSA)={r:+.2f}  mean entropy buried(RSA<0.2)={ent[d['rsa']<0.2].mean():.2f} exposed(RSA>0.5)={ent[d['rsa']>0.5].mean():.2f}",flush=True)
ent_all=np.array(ent_all);rsa_all=np.array(rsa_all);ss_all=np.array(ss_all)
print(f"== {MODEL} Exp4: per-protein Spearman(entropy,RSA) mean={np.mean(rho):+.3f} (min {min(rho):+.2f}, max {max(rho):+.2f}); pooled={spearmanr(ent_all,rsa_all).correlation:+.3f}, n={len(ent_all)}")
print("mean entropy by DSSP: "+", ".join(f"{k}={ent_all[ss_all==k].mean():.2f}" for k in "HE-"))
# ---- Exp 5 ----
seqs=read_fasta("../data/seqs/human_sp_80_250.fasta",NSEQ//2)+read_fasta("../data/seqs/ecoli_sp_80_250.fasta",NSEQ//2)
S=np.zeros((20,20)); cnt=np.zeros(20)
for k,s in enumerate(seqs):
    P=masked_marginals(s); idx=np.array([AAS.index(c) for c in s])
    np.add.at(S,idx,np.log(P+1e-9)); np.add.at(cnt,idx,1)
    if k%20==0: print("exp5 seq",k,flush=True)
S/=cnt[:,None]   # S[a,b]=mean log P(b | wt=a masked)
Ssym=(S+S.T)/2; iu=np.triu_indices(20,1)
B=blosum62(); R=snv_reachability(); Rs=(R+R.T)/2
def physchem_dist():
    cols=[]
    for tab in (KD,VOL,CHARGE,POLARITY,AROMATIC):
        v=np.array([tab[a] for a in AAS],float); v=(v-v.mean())/v.std(); cols.append(np.abs(v[:,None]-v[None,:]))
    return cols
PC=physchem_dist()
def fit(target, snv):
    X=sm.add_constant(np.c_[B[iu],*[c[iu] for c in PC],snv[iu]]); y=(target-target.mean())/target.std()
    f=sm.OLS(y,X).fit(); return f.params[-1],f.tvalues[-1],f.pvalues[-1],f.rsquared
def random_code_snv(rng):
    """permute amino acids across codon blocks (standard null for genetic-code structure)."""
    perm=dict(zip(AAS,rng.permutation(list(AAS))))
    R=np.zeros((20,20))
    for i,a in enumerate(AAS):
        codons=[c for c,x in CODON_AA.items() if x in AAS and perm[x]==a]
        for c in codons:
            for pos in range(3):
                for nb in BASES:
                    if nb==c[pos]: continue
                    x=CODON_AA[c[:pos]+nb+c[pos+1:]]
                    if x in AAS and perm[x]!=a: R[i,AAS.index(perm[x])]+=1
        R[i]/=len(codons)*9
    return (R+R.T)/2
rng=np.random.default_rng(0)
print(f"\n== {MODEL} Exp5: model substitution matrix S[a,b]=mean log P(b|a masked) over {len(seqs)} seqs ==")
print(f"Spearman(S, BLOSUM62) = {spearmanr(Ssym[iu],B[iu]).correlation:+.3f};  Spearman(S, SNV-reachability) = {spearmanr(Ssym[iu],Rs[iu]).correlation:+.3f}")
coef,t,p,r2=fit(Ssym[iu],Rs)
print(f"OLS S ~ BLOSUM62 + 5 physchem distances + SNV: SNV coef={coef:+.3f} t={t:+.2f} p={p:.1e} (R2={r2:.2f})")
null=np.array([fit(Ssym[iu],random_code_snv(rng))[1] for _ in range(500)])
print(f"random-genetic-code null for the SNV t-stat: mean {null.mean():+.2f}, sd {null.std():.2f}; real t={t:+.2f}; empirical p = {(null>=t).mean():.3f}")
# same test for the input-embedding similarity (exp1 follow-up with physchem controls)
tok2,m2=load_esm(MODEL); ids=[tok2.convert_tokens_to_ids(a) for a in AAS]; E=m2.esm.embeddings.word_embeddings.weight[ids].detach().numpy() if hasattr(m2,'esm') else m2.embeddings.word_embeddings.weight[ids].detach().numpy()
En=E/np.linalg.norm(E,axis=1,keepdims=True); Cs=(En@En.T)
coef2,t2,p2,r22=fit(Cs[iu],Rs); null2=np.array([fit(Cs[iu],random_code_snv(rng))[1] for _ in range(500)])
print(f"input-embedding cosine ~ BLOSUM62 + physchem + SNV: SNV t={t2:+.2f} p={p2:.1e}; random-code null mean {null2.mean():+.2f} sd {null2.std():.2f}; empirical p={(null2>=t2).mean():.3f}")
# directional asymmetry: is S[a,b] asymmetric in a way BLOSUM (symmetric) cannot capture? e.g. small->large vs large->small
asym=S-S.T; vol=np.array([VOL[a] for a in AAS]); dv=vol[None,:]-vol[:,None]  # dv[a,b] = vol(b)-vol(a)
print(f"asymmetry: corr(S[a,b]-S[b,a], vol(b)-vol(a)) = {pearsonr(asym[iu],dv[iu])[0]:+.3f}  (negative => model finds substituting to a LARGER residue less likely than the reverse)")
json.dump(dict(model=MODEL,exp4=dict(rho=rho,pooled=float(spearmanr(ent_all,rsa_all).correlation),ent_by_ss={k:float(ent_all[ss_all==k].mean()) for k in "HE-"}),
               exp5=dict(S=S.tolist(),rho_blosum=float(spearmanr(Ssym[iu],B[iu]).correlation),rho_snv=float(spearmanr(Ssym[iu],Rs[iu]).correlation),snv_t=float(t),snv_p=float(p),null_mean=float(null.mean()),null_sd=float(null.std()),emp_p=float((null>=t).mean()),
                         emb_snv_t=float(t2),emb_emp_p=float((null2>=t2).mean()),asym_vol_r=float(pearsonr(asym[iu],dv[iu])[0]))),open(f"../results/exp45_{MODEL.split('/')[-1]}.json","w"))
