"""Exp B2: interrogate CHGNet as an oracle: for 62 binary AX compounds, which of rock-salt (CN6),
CsCl (CN8), zinc-blende (CN4) does it prefer, and does its preference follow Pauling's radius-ratio
rule or Phillips ionicity?"""
import json, numpy as np, warnings, sys; warnings.filterwarnings("ignore")
from pymatgen.core import Structure, Lattice, Species, Element
from chgnet.model import CHGNet, StructOptimizer
import torch; torch.set_num_threads(1)
m=CHGNet.load(verbose=False); relaxer=StructOptimizer(model=m)
systems={ # (cation ox, anion ox, cations, anions, experimental coordination number)
 "alkali_halide":(1,-1,"Li Na K Rb Cs".split(),"F Cl Br I".split()),
 "alkaline_earth_chalc":(2,-2,"Mg Ca Sr Ba".split(),"O S Se Te".split()),
 "IIB_VI":(2,-2,"Zn Cd".split(),"O S Se Te".split()),
 "III_V":(3,-3,"Al Ga In".split(),"N P As Sb".split()),
 "IB_halide":(1,-1,"Cu Ag".split(),"Cl Br I".split()),
}
# experimental ground-truth coordination (ambient): default per family, with exceptions
exp_cn={}
for A in "Li Na K Rb".split():
    for X in "F Cl Br I".split(): exp_cn[A+X]=6
for X in "F".split(): exp_cn["Cs"+X]=6
for X in "Cl Br I".split(): exp_cn["Cs"+X]=8
for A in "Mg Ca Sr Ba".split():
    for X in "O S Se Te".split(): exp_cn[A+X]=6
exp_cn["MgTe"]=4  # wurtzite
for A in "Zn Cd".split():
    for X in "O S Se Te".split(): exp_cn[A+X]=4  # wurtzite/zinc-blende
exp_cn["CdO"]=6
for A in "Al Ga In".split():
    for X in "N P As Sb".split(): exp_cn[A+X]=4
for X in "Cl Br I".split(): exp_cn["Cu"+X]=4
exp_cn["AgCl"]=6; exp_cn["AgBr"]=6; exp_cn["AgI"]=4
def build(A,X,r):
    out={}
    out["RS"]=Structure.from_spacegroup("Fm-3m",Lattice.cubic(2*r),[A,X],[[0,0,0],[0.5,0.5,0.5]]).get_primitive_structure()
    out["CsCl"]=Structure.from_spacegroup("Pm-3m",Lattice.cubic(2*r/np.sqrt(3)),[A,X],[[0,0,0],[0.5,0.5,0.5]])
    out["ZB"]=Structure.from_spacegroup("F-43m",Lattice.cubic(4*r/np.sqrt(3)),[A,X],[[0,0,0],[0.25,0.25,0.25]]).get_primitive_structure()
    return out
import os
rows=[]; done={}
if os.path.exists("../results/expB2_radius_ratio.json"):
    done={r["comp"]:r for r in json.load(open("../results/expB2_radius_ratio.json"))}
for fam,(oa,ox,cats,ans) in systems.items():
    for A in cats:
        for X in ans:
            FALLBACK={("N",-3):1.46,("P",-3):2.12,("As",-3):2.22,("Sb",-3):2.45,("Cu",1):0.77,("Ag",1):1.15,("Al",3):0.535,("Ga",3):0.62,("In",3):0.80}
            def rad(el,ox):
                try: v=Species(el,ox).ionic_radius
                except Exception: v=None
                if v is None: v=FALLBACK.get((el,ox)) or float(Element(el).atomic_radius)
                return float(v)
            ra=rad(A,oa); rx=rad(X,ox)
            if A+X in done: rows.append(done[A+X]); continue
            res={}
            for name,s in build(A,X,ra+rx).items():
                try:
                    r=relaxer.relax(s,fmax=0.05,steps=400,verbose=False)
                    fs=r["final_structure"]; e=float(m.predict_structure(fs)["e"])  # eV/atom
                    res[name]=dict(e=e,vol=fs.volume/len(fs),a=fs.lattice.a)
                except Exception as ex:
                    res[name]=dict(e=np.nan,err=str(ex))
            dEN=abs(Element(A).X-Element(X).X)
            pred=min(res,key=lambda k:res[k]["e"])
            row=dict(family=fam,A=A,X=X,comp=A+X,r_ratio=ra/rx,dEN=dEN,exp_cn=exp_cn[A+X],
                     e_RS=res["RS"]["e"],e_CsCl=res["CsCl"]["e"],e_ZB=res["ZB"]["e"],pred=pred,pred_cn={"RS":6,"CsCl":8,"ZB":4}[pred])
            rows.append(row); json.dump(rows,open("../results/expB2_radius_ratio.json","w"),indent=1)
            print(f"{A+X:5s} r+/r-={ra/rx:.2f} dEN={dEN:.2f} exp CN{exp_cn[A+X]} | E(ZB-RS)={res['ZB']['e']-res['RS']['e']:+.3f} E(CsCl-RS)={res['CsCl']['e']-res['RS']['e']:+.3f} eV/at -> model {pred} CN{row['pred_cn']} {'OK' if row['pred_cn']==exp_cn[A+X] else 'xx'}",flush=True)
json.dump(rows,open("../results/expB2_radius_ratio.json","w"),indent=1)
acc=np.mean([r["pred_cn"]==r["exp_cn"] for r in rows]); print("model vs experiment agreement:",acc,"n=",len(rows))
