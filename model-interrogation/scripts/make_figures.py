"""Figures for the model-interrogation report. Palette: validated reference palette (blue/orange/aqua), sequential blue ramp."""
import json, os, sys, numpy as np, matplotlib, matplotlib.ticker
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
R="../results/"; F="../figures/"
SURF="#fcfcfb"; INK="#0b0b0b"; INK2="#52514e"; GRID="#e6e5e1"
S1,S2,S3="#2a78d6","#eb6834","#1baf7a"; OTHER="#9a9890"
SEQ=LinearSegmentedColormap.from_list("seqblue",["#cde2fb","#86b6ef","#3987e5","#1c5cab","#0d366b"])
plt.rcParams.update({"figure.facecolor":SURF,"axes.facecolor":SURF,"axes.edgecolor":GRID,"axes.labelcolor":INK2,"xtick.color":INK2,"ytick.color":INK2,"text.color":INK,
    "axes.grid":True,"grid.color":GRID,"grid.linewidth":0.6,"axes.spines.top":False,"axes.spines.right":False,"font.size":9,"axes.titlesize":10,"axes.titleweight":"bold","legend.frameon":False,"savefig.dpi":160})
def ok(f): return os.path.exists(R+f)
def save(fig,name): fig.tight_layout(); fig.savefig(F+name,facecolor=SURF); plt.close(fig); print("wrote",name)

# Fig 1: ESM-2 amino-acid embedding PCA coloured by hydropathy
if ok("exp1_esm2_t12_35M_UR50D.json"):
    sys.path.insert(0,'.'); from protlib import AAS, KD
    d=json.load(open(R+"exp1_esm2_t12_35M_UR50D.json")); Z=np.array(d["Z"]); kd=np.array([KD[a] for a in AAS])
    fig,ax=plt.subplots(figsize=(5.2,4.2))
    sc=ax.scatter(Z[:,0],Z[:,1],c=kd,cmap=SEQ,s=160,edgecolor=SURF,linewidth=1.5)
    for a,(x,y) in zip(AAS,Z): ax.text(x,y,a,ha="center",va="center",fontsize=8,color=SURF if KD[a]>0 else INK,fontweight="bold")
    cb=fig.colorbar(sc,ax=ax,shrink=0.8); cb.set_label("Kyte-Doolittle hydropathy",color=INK2); cb.outline.set_visible(False)
    ax.set_xlabel(f"PC1 ({d['expl'][0]:.0%} var): polarity / hydropathy axis"); ax.set_ylabel(f"PC2 ({d['expl'][1]:.0%} var): size / aromaticity axis")
    ax.set_title("ESM-2 35M input embedding of the 20 amino acids\nPCA recovers the hydropathy axis (colour = textbook value)")
    save(fig,"fig1_esm_aa_pca.png")

# Fig 2: CHGNet element embedding PCA
if ok("expB1_chgnet_elements.json"):
    d=json.load(open(R+"expB1_chgnet_elements.json")); Z=np.array(d["pca"]); sym=d["symbols"]; blk=d["block"]
    col={"s":S1,"p":S2,"d":S3,"f":OTHER}
    fig,ax=plt.subplots(figsize=(6.2,4.8))
    for b,lab in [("s","s-block"),("p","p-block"),("d","d-block"),("f","f-block (other)")]:
        idx=[i for i in range(len(sym)) if blk[i]==b]
        ax.scatter(Z[idx,0],Z[idx,1],s=60,color=col[b],edgecolor=SURF,linewidth=1,label=lab,zorder=3)
    for i,s in enumerate(sym):
        if blk[i]!="f" or s in ("La","Ce","U","Th"): ax.text(Z[i,0],Z[i,1]+0.06,s,ha="center",va="bottom",fontsize=6.5,color=INK)
    ax.legend(loc="upper right",fontsize=8); ax.set_xlabel(f"PC1 ({d['expl'][0]:.0%} var): radius / electronegativity"); ax.set_ylabel(f"PC2 ({d['expl'][1]:.0%} var): melting point / max oxidation state")
    ax.set_title("CHGNet learned element embedding (94 elements, 64-d)\nnearest neighbour shares the group 56% of the time (chance 9%)")
    save(fig,"fig2_chgnet_element_pca.png")

# Fig 3: attention vs relative offset for structure-periodic heads
if ok("exp2_esm2_t12_35M_UR50D.json"):
    d=json.load(open(R+"exp2_esm2_t12_35M_UR50D.json")); prof=np.array(d["profile"]); offs=np.array(d["offsets"])
    picks=[(1,5,"L1H5: i → i+4 (α-helix H-bond partner)",S1),(2,12,"L2H12: i → i+3 (3₁₀ / helix turn)",S2),(1,16,"L1H16: i → i−2 (β-strand same face)",S3)]
    fig,ax=plt.subplots(figsize=(6,3.6))
    for l,h,lab,c in picks: ax.plot(offs,prof[l,h],color=c,linewidth=2,label=lab); 
    ax.axvline(0,color=GRID,linewidth=1); ax.set_xlabel("relative offset j − i (residues)"); ax.set_ylabel("mean attention weight")
    ax.set_xticks(range(-16,17,4)); ax.legend(fontsize=8,loc="upper left"); ax.set_title("ESM-2 35M: early-layer heads attend at fixed structural offsets\n(average over 300 UniProt sequences)")
    save(fig,"fig3_attention_offsets.png")

# Fig 4: best contact head vs true contact map
if ok("exp3_esm2_t30_150M_UR50D.json"):
    import torch; from protlib import load_pdb, contact_map, load_esm
    d=json.load(open(R+"exp3_esm2_t30_150M_UR50D.json")); hid=d["top_heads"][0]; H=20; l,h=hid//H,hid%H
    tok,m=load_esm("facebook/esm2_t30_150M_UR50D"); p=load_pdb("../data/pdb/1TEN.pdb"); s=p["seq"]; n=len(s); C,_=contact_map(p["cb"])
    with torch.no_grad(): A=m(**tok(s,return_tensors="pt"),output_attentions=True).attentions[l][0,h,1:-1,1:-1].numpy()
    A=A+A.T; M=np.zeros((n,n)); iu=np.triu_indices(n,1); M[iu]=A[iu]/A[iu].max(); il=np.tril_indices(n,-1); M[il]=C[il]*1.0
    fig,ax=plt.subplots(figsize=(4.8,4.6)); ax.imshow(M,cmap=SEQ,vmin=0,vmax=1,interpolation="nearest"); ax.grid(False)
    ax.set_title(f"1TEN (fibronectin III): attention head L{l}H{h} of ESM-2 150M\nupper = attention, lower = true Cβ contacts < 8 Å"); ax.set_xlabel("residue"); ax.set_ylabel("residue")
    save(fig,"fig4_contact_head_1TEN.png")

# Fig 5: radius-ratio rule
if ok("expB2_radius_ratio.json"):
    rows=json.load(open(R+"expB2_radius_ratio.json")); rows=[r for r in rows if r["e_RS"]==r["e_RS"]]
    fig,axs=plt.subplots(1,2,figsize=(9,3.9),sharex=True)
    cn_col={4:S2,6:S1,8:S3}
    for ax,key,lab in [(axs[0],"e_ZB","E(zinc-blende, CN4) − E(rock-salt, CN6)"),(axs[1],"e_CsCl","E(CsCl-type, CN8) − E(rock-salt, CN6)")]:
        for cn,c in cn_col.items():
            rr=[r for r in rows if r["exp_cn"]==cn]
            ax.scatter([r["r_ratio"] for r in rr],[r[key]-r["e_RS"] for r in rr],color=c,s=38,edgecolor=SURF,linewidth=0.8,label=f"experiment: CN{cn}",zorder=3)
        for r in rows:
            if abs(r[key]-r["e_RS"])<0.08 or r["comp"] in ("CsCl","CsI","CsF","AgI","AgCl","MgTe","CdO","ZnO","CuCl","InN","AlN","BaO","LiI","MgO"): ax.annotate(r["comp"],(r["r_ratio"],r[key]-r["e_RS"]),fontsize=6,color=INK2,xytext=(3,3),textcoords="offset points")
        ax.axhline(0,color=INK2,linewidth=1); 
        for v in (0.414,0.732): ax.axvline(v,color=GRID,linewidth=1.2,linestyle="--")
        ax.set_xlabel("Shannon radius ratio r₊ / r₋"); ax.set_ylabel(lab+"  [eV/atom]"); ax.set_xscale("log"); ax.set_xticks([0.3,0.414,0.5,0.732,1.0,1.5]); ax.set_xticklabels(["0.3","0.414","0.5","0.732","1.0","1.5"]); ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    axs[0].legend(fontsize=8,loc="upper right"); fig.suptitle("CHGNet's polymorph preference vs Pauling's radius-ratio thresholds (dashed): 62 binary AX compounds",fontweight="bold",fontsize=10)
    save(fig,"fig5_radius_ratio.png")

# Fig 6: Hund's rule
if ok("expB3_hund.json"):
    rows=json.load(open(R+"expB3_hund.json")); fig,ax=plt.subplots(figsize=(5.6,3.6))
    ax.plot([r[1] for r in rows],[r[2] for r in rows],color=S2,linewidth=2,marker="o",markersize=6,label="Hund's rule (high-spin d-count)")
    ax.plot([r[1] for r in rows],[r[3] for r in rows],color=S1,linewidth=2,marker="o",markersize=6,label="CHGNet predicted |moment| on M")
    for r in rows: ax.text(r[1],r[3]-0.45,r[0],ha="center",fontsize=7,color=INK2)
    ax.set_xlabel("d-electron count of M²⁺ in rock-salt MO"); ax.set_ylabel("magnetic moment (μB)"); ax.set_xticks(range(1,11)); ax.legend(fontsize=8,loc="upper right")
    ax.set_title("CHGNet reproduces the Hund's-rule arc across 3d monoxides (r = 0.94)\nand fails only where its DFT training data fails (Sc, Ti)")
    save(fig,"fig6_hund.png")

# Fig 7: HyenaDNA period-3 loss
if ok("expD_hyenadna.json"):
    d=json.load(open(R+"expD_hyenadna.json")); L=d["loss"]
    fig,ax=plt.subplots(figsize=(5.2,3.4)); w=0.26; x=np.arange(3)
    for k,(reg,c) in enumerate([("CDS",S1),("UTR5",S2),("UTR3",S3)]):
        ax.bar(x+(k-1)*w,L[reg]["means"],width=w-0.03,color=c,label={"CDS":"coding sequence","UTR5":"5′ UTR","UTR3":"3′ UTR"}[reg])
    ax.set_xticks(x); ax.set_xticklabels(["position 1","position 2","position 3 (wobble)"]); ax.set_ylabel("per-base loss (nats)"); ax.set_ylim(min(min(v["means"]) for v in L.values())-0.05,None)
    ax.legend(fontsize=8); ax.set_title(f"HyenaDNA (0.4M, human genome): loss by position mod 3\n({d['n_tx']} RefSeq mRNAs; frame is only defined in the CDS)")
    save(fig,"fig7_hyenadna_frame.png")

# Fig 8: ubiquitin -- conservation beyond burial picks out the functional surface
if ok("exp3_esm2_t30_150M_UR50D.json"):
    import torch; from protlib import load_pdb, load_esm, AAS
    tok,m=load_esm("facebook/esm2_t30_150M_UR50D",mlm=True); aa_ids=torch.tensor([tok.convert_tokens_to_ids(a) for a in AAS])
    d=load_pdb("../data/pdb/1UBQ.pdb"); s=d["seq"]; n=len(s); enc=tok(s,return_tensors="pt")["input_ids"][0]
    with torch.no_grad():
        X=enc.repeat(n,1)
        for i in range(n): X[i,i+1]=tok.mask_token_id
        P=torch.softmax(m(input_ids=X).logits[torch.arange(n),torch.arange(n)+1][:,aa_ids],-1).numpy()
    ent=-(P*np.log(P+1e-12)).sum(1); rsa=d["rsa"]
    func={8,44,68,70,6,11,48,63,72,73,74,75,76}  # I44 patch, TEK box, linkage lysines, C-terminal tail
    fig,ax=plt.subplots(figsize=(5.6,4))
    isf=np.array([num in func for num in d["nums"]])
    ax.scatter(rsa[~isf],ent[~isf],s=34,color=S1,edgecolor=SURF,linewidth=0.8,label="other residues",zorder=3)
    ax.scatter(rsa[isf],ent[isf],s=46,color=S2,edgecolor=SURF,linewidth=0.8,label="known functional surface / tail",zorder=4)
    for i in range(n):
        if (rsa[i]>0.35 and ent[i]<0.9) or ent[i]<0.1 and rsa[i]>0.5: ax.annotate(f"{s[i]}{d['nums'][i]}",(rsa[i],ent[i]),fontsize=7,color=INK2,xytext=(4,(-9 if s[i]+str(d['nums'][i]) in ("K6","G75") else 2)),textcoords="offset points")
    ax.set_xlabel("relative solvent accessibility (1UBQ crystal structure)"); ax.set_ylabel("ESM-2 150M masked-prediction entropy (nats)")
    ax.legend(fontsize=8,loc="upper left"); ax.set_title("Ubiquitin: residues the model holds fixed despite being exposed\nare the E1/E2-recognition tail and the I44 / TEK-box surface")
    save(fig,"fig8_ubiquitin_surface.png")
