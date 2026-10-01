"""Exp B3: does CHGNet know Hund's rule?  Predicted magnetic moments on M2+ in rock-salt MO across the 3d row."""
import numpy as np, warnings; warnings.filterwarnings("ignore")
from pymatgen.core import Structure, Lattice
from chgnet.model import CHGNet
import torch; torch.set_num_threads(1)
m=CHGNet.load(verbose=False)
d_count={"Sc":1,"Ti":2,"V":3,"Cr":4,"Mn":5,"Fe":6,"Co":7,"Ni":8,"Cu":9,"Zn":10}
hund_hs={1:1,2:2,3:3,4:4,5:5,6:4,7:3,8:2,9:1,10:0}
a_exp={"TiO":4.18,"VO":4.06,"MnO":4.44,"FeO":4.33,"CoO":4.26,"NiO":4.18}
print("rock-salt MO: M  d-count  Hund high-spin  CHGNet |magmom(M)|  magmom(O)")
rows=[]
for M,d in d_count.items():
    a=a_exp.get(M+"O",4.25)
    s=Structure.from_spacegroup("Fm-3m",Lattice.cubic(a),[M,"O"],[[0,0,0],[0.5,0.5,0.5]])
    p=m.predict_structure(s)
    mm=p["m"]; mM=np.mean([abs(x) for x,site in zip(mm,s) if site.specie.symbol==M]); mO=np.mean([abs(x) for x,site in zip(mm,s) if site.specie.symbol=="O"])
    rows.append((M,d,hund_hs[d],float(mM),float(mO))); print(f"{M:3s} d{d:<2d} {hund_hs[d]:>6d} μB      {mM:6.2f} μB       {mO:5.2f}")
from scipy.stats import pearsonr, spearmanr
x=[r[2] for r in rows]; y=[r[3] for r in rows]
print(f"Pearson r(Hund high-spin, CHGNet magmom)={pearsonr(x,y)[0]:.3f}, Spearman={spearmanr(x,y).correlation:.3f}")
# also: same metal, different oxidation state -> does magmom shift by one electron? (Fe2+ in FeO vs Fe3+ in Fe2O3 corundum)
fe2o3=Structure.from_spacegroup("R-3c",Lattice.hexagonal(5.035,13.75),["Fe","O"],[[0,0,0.3553],[0.3059,0,0.25]])
p=m.predict_structure(fe2o3); print("Fe2O3 (Fe3+, d5 -> Hund 5): mean |magmom(Fe)| =",round(float(np.mean([abs(x) for x,site in zip(p['m'],fe2o3) if site.specie.symbol=='Fe'])),2))
import json; json.dump(rows,open("../results/expB3_hund.json","w"))
