from DNAToolKit import *
from colorama import init
from utilities import colored
import random

rndDNAStr=''.join([random.choice(Nucleotides) for nuc in range(20)])
DNAStr=validateSeq(rndDNAStr)
print("\n seqeunce\n"+colored(DNAStr)+"\n")
print("[1] seqeuncelength")
print(len(DNAStr))
print("\n[2] Nuleotide Frequency")
print(countNucFrequency(DNAStr))
print("\n[3] DNA/RNA Transcription")
print(transcription(DNAStr))
print("5`-"+DNAStr+"-3`")
print("   "+''.join(['|'for c in range(len(DNAStr))]))
print("3`-"+reverseComplement(DNAStr)+"-5`")