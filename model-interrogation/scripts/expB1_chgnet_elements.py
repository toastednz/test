"""Exp B1: does CHGNet's learned element embedding recover the periodic table?"""
import json, numpy as np, torch, warnings; warnings.filterwarnings("ignore")
from chgnet.model import CHGNet
from pymatgen.core import Element
from scipy.stats import pearsonr
from sklearn.linear_model import RidgeCV, LogisticRegressionCV
from sklearn.model_selection import LeaveOneOut, cross_val_predict, cross_val_score, StratifiedKFold
from sklearn.decomposition import PCA
m=CHGNet.load(verbose=False)
emb=m.atom_embedding.embedding.weight.detach().numpy() if hasattr(m.atom_embedding,"embedding") else None
if emb is None:
    for n,p in m.named_parameters():
        if "atom_embedding" in n: emb=p.detach().numpy(); print("using",n)
print("embedding shape",emb.shape)
# CHGNet indexes atomic number Z -> row Z-1 (max_num_elements=94)
Zs=list(range(1,95)); els=[Element.from_Z(z) for z in Zs]
E=emb[:94]
def safe(f):
    try: v=f(); return float(v) if v is not None else np.nan
    except Exception: return np.nan
props={
 "electronegativity":[safe(lambda e=e:e.X) for e in els],
 "atomic_radius":[safe(lambda e=e:e.atomic_radius) for e in els],
 "group":[e.group for e in els],"row":[e.row for e in els],"Z":Zs,
 "log_mass":[np.log(float(e.atomic_mass)) for e in els],
 "ionization_energy":[safe(lambda e=e:e.ionization_energy) for e in els],
 "electron_affinity":[safe(lambda e=e:e.electron_affinity) for e in els],
 "melting_point":[safe(lambda e=e:e.melting_point) for e in els],
 "max_oxidation_state":[safe(lambda e=e:e.max_oxidation_state) for e in els],
 "min_oxidation_state":[safe(lambda e=e:e.min_oxidation_state) for e in els],
 "n_valence(s+p+d outer)":[safe(lambda e=e:sum(n for (sh,orb,n) in e.full_electronic_structure if sh>=e.row-1 and orb in "spd" and not (orb=="d" and sh==e.row))) for e in els],
}
print("\n== LOO ridge probes: CHGNet element embedding -> property (Pearson r) ==")
out={}
for k,v in props.items():
    y=np.array(v,float); ok=~np.isnan(y)
    pred=cross_val_predict(RidgeCV(alphas=np.logspace(-2,4,25)),E[ok],y[ok],cv=LeaveOneOut())
    r=pearsonr(pred,y[ok])[0]; out[k]=dict(r=float(r),n=int(ok.sum()))
    print(f"{k:25s} r={r:+.3f}  (n={ok.sum()})")
# categorical: block (s/p/d/f) and is_metal via CV logistic
blocks=np.array([e.block for e in els]); metal=np.array([e.is_metal for e in els])
cv=StratifiedKFold(5,shuffle=True,random_state=0)
print("\nblock (s/p/d/f) 5-fold accuracy:",round(cross_val_score(LogisticRegressionCV(max_iter=3000),E,blocks,cv=cv).mean(),3),"| chance(majority)=",round(max(np.mean(blocks==b) for b in set(blocks)),3))
print("is_metal 5-fold accuracy:",round(cross_val_score(LogisticRegressionCV(max_iter=3000),E,metal,cv=cv).mean(),3),"| chance=",round(max(metal.mean(),1-metal.mean()),3))
# nearest-neighbour structure
En=E/np.linalg.norm(E,axis=1,keepdims=True); S=En@En.T; np.fill_diagonal(S,-9)
nn=S.argmax(1)
same_group=np.mean([els[i].group==els[nn[i]].group for i in range(94)])
same_block=np.mean([els[i].block==els[nn[i]].block for i in range(94)])
adj_Z=np.mean([abs(Zs[i]-Zs[nn[i]])==1 for i in range(94)])
print(f"\nnearest neighbour in embedding space: same group {same_group:.2f} (chance ~{np.mean([[els[i].group==els[j].group for j in range(94) if j!=i] for i in range(94)]):.2f}), same block {same_block:.2f}, adjacent Z {adj_Z:.2f}")
print("examples (element -> nearest):", ", ".join(f"{els[i].symbol}->{els[nn[i]].symbol}" for i in [0,2,5,6,7,8,10,11,13,16,18,19,25,28,33,34,36,46,52,54,78,91]))
pca=PCA(4).fit(E); Z=pca.transform(E)
print("PCA explained:",np.round(pca.explained_variance_ratio_,3))
for k in range(3):
    best=sorted(((abs(pearsonr(Z[~np.isnan(np.array(v,float)),k],np.array(v,float)[~np.isnan(np.array(v,float))])[0]),n) for n,v in props.items()),reverse=True)[:3]
    print(f"PC{k+1}: "+", ".join(f"{n} |r|={r:.2f}" for r,n in best))
json.dump(dict(probe=out,pca=Z[:,:3].tolist(),symbols=[e.symbol for e in els],group=[e.group for e in els],row=[e.row for e in els],block=list(blocks),nn=[els[nn[i]].symbol for i in range(94)],expl=pca.explained_variance_ratio_.tolist()),open("../results/expB1_chgnet_elements.json","w"))
