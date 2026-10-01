"""Shared helpers: PDB parsing, DSSP, SASA, genetic code, AA property tables, ESM loading."""
import numpy as np, torch, warnings
from Bio.PDB import PDBParser
from Bio.PDB.SASA import ShrakeRupley
from Bio.PDB.Polypeptide import three_to_index, index_to_one, is_aa
warnings.filterwarnings("ignore")

AAS = "ACDEFGHIKLMNPQRSTVWY"

# --- physicochemical tables (standard literature values) ---
KD = dict(A=1.8,R=-4.5,N=-3.5,D=-3.5,C=2.5,Q=-3.5,E=-3.5,G=-0.4,H=-3.2,I=4.5,L=3.8,K=-3.9,M=1.9,F=2.8,P=-1.6,S=-0.8,T=-0.7,W=-0.9,Y=-1.3,V=4.2)
VOL = dict(A=88.6,R=173.4,N=114.1,D=111.1,C=108.5,Q=143.8,E=138.4,G=60.1,H=153.2,I=166.7,L=166.7,K=168.6,M=162.9,F=189.9,P=112.7,S=89.0,T=116.1,W=227.8,Y=193.6,V=140.0)
MASS = dict(A=71.08,R=156.19,N=114.10,D=115.09,C=103.14,Q=128.13,E=129.12,G=57.05,H=137.14,I=113.16,L=113.16,K=128.17,M=131.19,F=147.18,P=97.12,S=87.08,T=101.10,W=186.21,Y=163.18,V=99.13)
CHARGE = {a:0.0 for a in AAS}; CHARGE.update(K=1,R=1,D=-1,E=-1,H=0.1)
HELIX_DDG = dict(A=0,L=0.21,R=0.21,M=0.24,K=0.26,Q=0.39,E=0.40,I=0.41,W=0.49,S=0.50,Y=0.53,F=0.54,H=0.61,V=0.61,N=0.65,T=0.66,C=0.68,D=0.69,G=1.00,P=3.16)  # Pace & Scholtz 1998
CF_BETA = dict(A=0.83,R=0.93,N=0.89,D=0.54,C=1.19,Q=1.10,E=0.37,G=0.75,H=0.87,I=1.60,L=1.30,K=0.74,M=1.05,F=1.38,P=0.55,S=0.75,T=1.19,W=1.37,Y=1.47,V=1.70)
CF_ALPHA = dict(A=1.42,R=0.98,N=0.67,D=1.01,C=0.70,Q=1.11,E=1.51,G=0.57,H=1.00,I=1.08,L=1.21,K=1.16,M=1.45,F=1.13,P=0.57,S=0.77,T=0.83,W=1.08,Y=0.69,V=1.06)
PI = dict(A=6.00,R=10.76,N=5.41,D=2.77,C=5.07,Q=5.65,E=3.22,G=5.97,H=7.59,I=6.02,L=5.98,K=9.74,M=5.74,F=5.48,P=6.30,S=5.68,T=5.60,W=5.89,Y=5.66,V=5.96)
POLARITY = dict(A=8.1,R=10.5,N=11.6,D=13.0,C=5.5,Q=10.5,E=12.3,G=9.0,H=10.4,I=5.2,L=4.9,K=11.3,M=5.7,F=5.2,P=8.0,S=9.2,T=8.6,W=5.4,Y=6.2,V=5.9)
NCODONS = dict(A=4,R=6,N=2,D=2,C=2,Q=2,E=2,G=4,H=2,I=3,L=6,K=2,M=1,F=2,P=4,S=6,T=4,W=1,Y=2,V=4)
AROMATIC = {a:float(a in "FWY") for a in AAS}
MAX_ASA = dict(A=129,R=274,N=195,D=193,C=167,Q=225,E=223,G=104,H=224,I=197,L=201,K=236,M=224,F=240,P=159,S=155,T=172,W=285,Y=263,V=174)  # Tien 2013 theoretical
PROPS = {"hydropathy(KD)":KD,"volume":VOL,"mass":MASS,"charge":CHARGE,"helix_ddG(Pace)":HELIX_DDG,"beta_prop(CF)":CF_BETA,"alpha_prop(CF)":CF_ALPHA,"pI":PI,"polarity(Grantham)":POLARITY,"n_codons":NCODONS,"aromatic":AROMATIC}

# --- standard genetic code ---
BASES="TCAG"
CODON_AA = {}
_aa = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
_i=0
for b1 in BASES:
    for b2 in BASES:
        for b3 in BASES:
            CODON_AA[b1+b2+b3]=_aa[_i]; _i+=1

def snv_reachability():
    """R[a,b] = fraction of codons of a from which a single-nucleotide change gives b."""
    R = np.zeros((20,20))
    for i,a in enumerate(AAS):
        codons=[c for c,x in CODON_AA.items() if x==a]
        for c in codons:
            for pos in range(3):
                for nb in BASES:
                    if nb==c[pos]: continue
                    c2=c[:pos]+nb+c[pos+1:]
                    x=CODON_AA[c2]
                    if x in AAS and x!=a:
                        R[i,AAS.index(x)] += 1
        R[i]/= (len(codons)*9)
    return R

def blosum62():
    from Bio.Align import substitution_matrices
    B = substitution_matrices.load("BLOSUM62")
    M = np.array([[B[a][b] for b in AAS] for a in AAS], float)
    return M

# --- PDB ---
def load_pdb(path, chain_id=None):
    s = PDBParser(QUIET=True).get_structure("x", path)
    model = next(iter(s))
    chain = model[chain_id] if chain_id else next(iter(model))
    residues=[r for r in chain if is_aa(r, standard=True) and "CA" in r and "N" in r and "C" in r and "O" in r]
    seq="".join(index_to_one(three_to_index(r.get_resname())) for r in residues)
    nums=[r.get_id()[1] for r in residues]
    gaps = sum(1 for a,b in zip(nums,nums[1:]) if b-a!=1)
    ca=np.array([r["CA"].coord for r in residues])
    cb=np.array([(r["CB"].coord if "CB" in r else r["CA"].coord) for r in residues])
    bb=np.array([[r[a].coord for a in ("N","CA","C","O")] for r in residues])  # (L,4,3)
    # SASA on the chain only (remove other chains/hetero so RSA reflects the monomer)
    for ch in list(model):
        if ch.id!=chain.id: model.detach_child(ch.id)
    for r in list(chain):
        if r not in residues: chain.detach_child(r.get_id())
    ShrakeRupley().compute(chain, level="R")
    rsa=np.array([min(r.sasa/MAX_ASA[a],1.5) for r,a in zip(residues,seq)])
    return dict(seq=seq, ca=ca, cb=cb, bb=bb, rsa=rsa, gaps=gaps, nums=nums, chain=chain.id)

def dssp_ss(bb):
    import pydssp
    ss = pydssp.assign(bb.astype(np.float64), out_type="c3")  # '-', 'H', 'E'
    return np.array(list(ss))

def contact_map(cb, cutoff=8.0):
    d=np.linalg.norm(cb[:,None,:]-cb[None,:,:],axis=-1)
    return (d<cutoff), d

# --- ESM ---
def load_esm(name="facebook/esm2_t12_35M_UR50D", mlm=False):
    from transformers import AutoTokenizer, EsmModel, EsmForMaskedLM
    tok=AutoTokenizer.from_pretrained(name)
    cls = EsmForMaskedLM if mlm else EsmModel
    m=cls.from_pretrained(name, attn_implementation="eager").eval()
    return tok,m

def read_fasta(path, maxn=None):
    seqs=[];cur=[]
    for line in open(path):
        if line.startswith(">"):
            if cur: seqs.append("".join(cur)); cur=[]
        else: cur.append(line.strip())
    if cur: seqs.append("".join(cur))
    seqs=[s for s in seqs if set(s)<=set(AAS)]
    return seqs[:maxn] if maxn else seqs
