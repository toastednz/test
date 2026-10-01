"""Exp D: interrogate a DNA language model (HyenaDNA tiny, trained on human genome, causal).
D1: does per-base loss show 3-periodicity inside CDS but not UTR  (model learned the reading frame)?
D2: does the model suppress in-frame stop codons specifically (model learned the genetic code's stops)?"""
import re, json, numpy as np, torch, urllib.request, time
from transformers import AutoModelForCausalLM, AutoTokenizer
torch.set_num_threads(1)
import sys; n=sys.argv[1] if len(sys.argv)>1 else 'LongSafari/hyenadna-tiny-1k-seqlen-hf'; TAG=n.split('hyenadna-')[1].split('-seqlen')[0]
tok=AutoTokenizer.from_pretrained(n,trust_remote_code=True); m=AutoModelForCausalLM.from_pretrained(n,trust_remote_code=True).eval()
base_ids={b:tok.convert_tokens_to_ids(b) for b in "ACGT"}
# fetch human RefSeq mRNAs with CDS annotation
def eutil(url):
    for k in range(4):
        try: return urllib.request.urlopen(url,timeout=60).read().decode()
        except Exception as e: time.sleep(2**k)
    raise RuntimeError(url)
ids=re.findall(r"<Id>(\d+)</Id>",eutil("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=srcdb_refseq%5Bprop%5D+AND+biomol_mrna%5Bprop%5D+AND+%22Homo+sapiens%22%5Borgn%5D+AND+1500%3A3500%5Bslen%5D&retmax=80"))
print("fetched",len(ids),"ids")
recs=[]
for chunk in range(0,len(ids),20):
    gb=eutil("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id="+",".join(ids[chunk:chunk+20])+"&rettype=gb&retmode=text")
    for rec in gb.split("//\n"):
        acc=re.search(r"^LOCUS\s+(\S+)",rec,re.M); cds=re.search(r"^\s+CDS\s+(\d+)\.\.(\d+)\s*$",rec,re.M); ori=rec.find("ORIGIN")
        if not(acc and cds and ori>0) or not acc.group(1).startswith("NM_"): continue
        seq=re.sub(r"[^acgt]","",rec[ori+6:]).upper()
        s,e=int(cds.group(1)),int(cds.group(2))
        if (e-s+1)%3!=0 or s<80 or len(seq)-e<80: continue
        recs.append(dict(acc=acc.group(1),seq=seq,cds=(s-1,e)))  # 0-based [s-1,e)
print("usable mRNAs:",len(recs))
def per_base_logp(seq,W=int(sys.argv[2]) if len(sys.argv)>2 else 1024,stride=None):
    stride=stride or W//2
    """log-prob of each base under the causal model, using sliding windows and keeping the right part."""
    ids=torch.tensor([[tok.convert_tokens_to_ids(c) for c in seq]]); L=ids.shape[1]
    lp=np.full((L,4),np.nan)
    with torch.no_grad():
        starts=list(range(0,max(1,L-W+1),stride)); 
        if starts[-1]!=max(0,L-W): starts.append(max(0,L-W))
        for st in starts:
            x=ids[:,st:st+W]; logits=m(input_ids=x).logits[0]  # W x V, logits[t] predicts token t+1
            lsm=torch.log_softmax(logits[:,[base_ids[b] for b in "ACGT"]],-1).numpy()
            lo=st+1 if st==0 else st+W//2
            for t in range(lo,min(st+W,L)): lp[t]=lsm[t-st-1]
    return lp
LOSS={"CDS":[[],[],[]],"UTR5":[[],[],[]],"UTR3":[[],[],[]]}
stop_in=[];stop_out=[]; stop_frame_detail={0:[],1:[],2:[]}
for r in recs:
    seq=r["seq"]; s,e=r["cds"]; lp=per_base_logp(seq); bidx={b:i for i,b in enumerate("ACGT")}
    nll=np.array([-lp[t,bidx[c]] if c in bidx else np.nan for t,c in enumerate(seq)])
    for t in range(1,len(seq)):
        if np.isnan(nll[t]): continue
        if s<=t<e: LOSS["CDS"][(t-s)%3].append(nll[t])
        elif t<s: LOSS["UTR5"][t%3].append(nll[t])
        else: LOSS["UTR3"][(t-e)%3].append(nll[t])
    # D2: at positions t where seq[t-2:t] in {TA,TG}, probability model assigns to completing a stop (TAA,TAG,TGA)
    for t in range(2,len(seq)):
        if np.isnan(lp[t,0]): continue
        two=seq[t-2:t]
        if two not in ("TA","TG"): continue
        p=np.exp(lp[t]); pstop=(p[0]+p[2]) if two=="TA" else p[0]  # TAA,TAG | TGA
        frame=(t-2-s)%3  # 0 => codon starts at t-2 in frame
        if s<=t-2 and t<e-3:  # inside CDS, excluding the real stop
            stop_frame_detail[frame].append(pstop)
            (stop_in if frame==0 else stop_out).append(pstop)
print("\n== D1: mean per-base NLL (nats) by position mod 3 ==")
out={}
for k,v in LOSS.items():
    means=[np.mean(x) for x in v]; sds=[np.std(x)/np.sqrt(len(x)) for x in v]
    out[k]=dict(means=means,n=[len(x) for x in v])
    print(f"{k:5s}: pos1 {means[0]:.3f}±{sds[0]:.3f}  pos2 {means[1]:.3f}±{sds[1]:.3f}  pos3 {means[2]:.3f}±{sds[2]:.3f}   (max-min = {max(means)-min(means):.3f}; n={sum(len(x) for x in v)})")
# periodicity strength: spectral power at 1/3 in CDS vs UTR3, per transcript
def pow3(x):
    x=np.array(x); x=x[~np.isnan(x)]; x=x-x.mean(); f=np.fft.rfft(x); k=int(round(len(x)/3)); return abs(f[k])**2/ (abs(f[1:])**2).mean()
P3={"CDS":[],"UTR3":[]}
for r in recs:
    seq=r["seq"]; s,e=r["cds"]; lp=per_base_logp(seq); bidx={b:i for i,b in enumerate("ACGT")}
    nll=np.array([-lp[t,bidx[c]] if c in bidx else np.nan for t,c in enumerate(seq)])
    if e-s>300 and len(seq)-e>300: P3["CDS"].append(pow3(nll[s:e][:300])); P3["UTR3"].append(pow3(nll[e:][:300]))
print(f"relative spectral power at period-3 (300-nt windows, {len(P3['CDS'])} transcripts): CDS median {np.median(P3['CDS']):.1f}x vs 3'UTR median {np.median(P3['UTR3']):.1f}x; CDS>UTR in {np.mean(np.array(P3['CDS'])>np.array(P3['UTR3'])):.0%}")
print("\n== D2: probability assigned to completing a stop codon after 'TA'/'TG' inside CDS ==")
print(f"in-frame (would create premature stop): mean p={np.mean(stop_in):.3f} (n={len(stop_in)});  out-of-frame: mean p={np.mean(stop_out):.3f} (n={len(stop_out)});  ratio={np.mean(stop_in)/np.mean(stop_out):.2f}")
print("by frame of the TA/TG dinucleotide:",{f:round(float(np.mean(v)),3) for f,v in stop_frame_detail.items()})
from scipy.stats import mannwhitneyu
print("Mann-Whitney in-frame vs out-of-frame p =",mannwhitneyu(stop_in,stop_out).pvalue)
json.dump(dict(loss=out,p3=P3,stop_in=float(np.mean(stop_in)),stop_out=float(np.mean(stop_out)),n_tx=len(recs)),open("../results/expD_hyenadna_"+TAG+".json","w"))
