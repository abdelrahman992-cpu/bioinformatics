import collections
from structures import *
def validateSeq(dna_seq):
    tmpseq=dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

def countNucFrequency(seq):
    #tmpFreqDict={"A":0,"C":0,"G":0,"T":0}
    #for nuc in seq:
        #tmpFreqDict[nuc]+=1
    #return tmpFreqDict
    return dict(collections.Counter(seq))
def transcription(seq):
    return seq.replace("T","U")
def reverseComplement(seq):
    return ''.join([DNAreverseComplement[nuc] for nuc in seq])[::-1]
def GCcontent(seq):
    return round((seq.count('C')+seq.count('G')) / len(seq) * 100)
def gc_content_subsec(seq, k=20):
        """GC Content in a DNA/RNA sub-sequence length k. k=20 by default"""
        res = []
        for i in range(0, len(seq) - k + 1, k):
            subseq = seq[i:i + k]
            res.append(
                round((subseq.count('C') + subseq.count('G')) / len(subseq) * 100))
        return res
