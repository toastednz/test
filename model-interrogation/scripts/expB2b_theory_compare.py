"""Which human theory does CHGNet's structure preference follow: Pauling radius-ratio (hard spheres) or
Phillips/Pauling ionicity (electronegativity difference)?"""
import json, numpy as np
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import cross_val_score, LeaveOneOut, cross_val_predict
from scipy.stats import pearsonr
rows=[r for r in json.load(open("../results/expB2_radius_ratio.json")) if r["e_RS"]==r["e_RS"]]
dE=np.array([r["e_ZB"]-r["e_RS"] for r in rows]); y=(dE<0).astype(int)  # 1 = model prefers 4-coordination
lr=np.log(np.array([r["r_ratio"] for r in rows])); en=np.array([r["dEN"] for r in rows]); yexp=np.array([r["exp_cn"]==4 for r in rows]).astype(int)
print(f"n={len(rows)}; model prefers CN4 (zinc-blende) in {y.sum()} compounds; experiment CN4 in {yexp.sum()}")
for name,X in [("log radius ratio (Pauling)",lr[:,None]),("electronegativity diff (ionicity)",en[:,None]),("both",np.c_[lr,en])]:
    acc=cross_val_score(LogisticRegression(),X,y,cv=LeaveOneOut()).mean()
    pred=cross_val_predict(LinearRegression(),X,dE,cv=LeaveOneOut()); r=pearsonr(pred,dE)[0]
    acc_exp=cross_val_score(LogisticRegression(),X,yexp,cv=LeaveOneOut()).mean()
    print(f"{name:38s}: LOO accuracy predicting MODEL's CN4-vs-CN6 choice = {acc:.2f};  LOO r for E(ZB)-E(RS) = {r:+.2f};  LOO accuracy predicting EXPERIMENT = {acc_exp:.2f}")
# where does the model put the CN4/CN6 boundary in dEN?
m=LogisticRegression().fit(en[:,None],y); print(f"model's ionicity boundary: dEN* = {-m.intercept_[0]/m.coef_[0][0]:.2f} (Pauling's 50%-ionic point is dEN≈1.7)")
# families at the same radius ratio but different ionicity
print("\nSame radius-ratio window 0.5-0.7, different ionicity:")
for r in sorted(rows,key=lambda r:r["dEN"]):
    if 0.5<=r["r_ratio"]<=0.7: print(f"  {r['comp']:5s} r+/r-={r['r_ratio']:.2f} dEN={r['dEN']:.2f}  E(ZB)-E(RS)={r['e_ZB']-r['e_RS']:+.3f}  model CN{r['pred_cn']} exp CN{r['exp_cn']}")
