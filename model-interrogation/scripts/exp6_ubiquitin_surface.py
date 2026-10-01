"""Exp 6: discovery-style query -- which ubiquitin residues does ESM-2 consider conserved *beyond* what burial explains?
Those should be the functional surface (I44 patch, K48/K63, C-terminal tail)."""
import sys, numpy as np, torch
sys.path.insert(0,'.'); from protlib import *
import statsmodels.api as sm
torch.set_num_threads(1)
MODEL=sys.argv[1] if len(sys.argv)>1 else "facebook/esm2_t30_150M_UR50D"
tok,m=load_esm(MODEL,mlm=True); aa_ids=torch.tensor([tok.convert_tokens_to_ids(a) for a in AAS]); mask_id=tok.mask_token_id
d=load_pdb("../data/pdb/1UBQ.pdb"); s=d["seq"]; n=len(s); ss=dssp_ss(d["bb"])
enc=tok(s,return_tensors="pt")["input_ids"][0]; P=np.zeros((n,20))
with torch.no_grad():
    X=enc.repeat(n,1)
    for i in range(n): X[i,i+1]=mask_id
    logits=m(input_ids=X).logits[torch.arange(n),torch.arange(n)+1][:,aa_ids]; P=torch.softmax(logits,-1).numpy()
ent=-(P*np.log(P+1e-12)).sum(1); pwt=np.array([P[i,AAS.index(c)] for i,c in enumerate(s)])
fit=sm.OLS(ent,sm.add_constant(d["rsa"])).fit(); resid=ent-fit.predict(sm.add_constant(d["rsa"]))
print(f"{MODEL} ubiquitin: Spearman(entropy,RSA)={np.corrcoef(np.argsort(np.argsort(ent)),np.argsort(np.argsort(d['rsa'])))[0,1]:+.2f}; slope entropy~RSA = {fit.params[1]:+.2f}")
known={"I44 patch":[8,44,68,70],"F4 patch":[2,4,12],"TEK box":[6,11],"D58 patch":[58],"Ub-linkage Lys":[6,11,27,29,33,48,63],"C-term tail":[71,72,73,74,75,76],"M1":[1]}
flag={}
for k,v in known.items():
    for r in v: flag.setdefault(r,[]).append(k)
order=np.argsort(resid)
print("\nMost conserved-beyond-burial residues (lowest residual entropy), with RSA and p(wt):")
for i in order[:16]:
    print(f"  {s[i]}{d['nums'][i]:<3d} RSA={d['rsa'][i]:.2f} ss={ss[i]} entropy={ent[i]:.2f} (expected {fit.predict([[1,d['rsa'][i]]])[0]:.2f}) p(wt)={pwt[i]:.2f}  {'; '.join(flag.get(d['nums'][i],[]))}")
exposed=[i for i in range(n) if d["rsa"][i]>0.4]
print(f"\nAmong {len(exposed)} exposed residues (RSA>0.4), the 10 most conserved: "+", ".join(f"{s[i]}{d['nums'][i]}" for i in sorted(exposed,key=lambda i:ent[i])[:10]))
print("Least conserved exposed: "+", ".join(f"{s[i]}{d['nums'][i]}" for i in sorted(exposed,key=lambda i:-ent[i])[:8]))
# enrichment: are known functional residues over-represented in the bottom quartile of residual entropy?
func=set(r for v in known.values() for r in v); q=order[:n//4]
inq=sum(d["nums"][i] in func for i in q); print(f"\nknown functional residues: {inq}/{len(q)} in the most-conserved-beyond-burial quartile vs {sum(d['nums'][i] in func for i in range(n))}/{n} overall (enrichment {inq/len(q)/(sum(d['nums'][i] in func for i in range(n))/n):.2f}x)")
