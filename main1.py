import colorama
from DNAToolKit import *
from colorama import Fore , Back,Style
from utilities import colored
import random
colorama.init()
rndDNAStr=''.join([random.choice(Nucleotides) for nuc in range(50)])
DNAStr=validateSeq(rndDNAStr)
print("\n seqeunce\n"+colored(DNAStr)+"\n")
print("[1] seqeuncelength")
print(len(DNAStr))
print("\n[2] Nuleotide Frequency")
print(colored(countNucFrequency(DNAStr)))
print("\n[3] DNA/RNA Transcription")
print(colored(transcription(DNAStr)))
print("[4] DNA String + complement+ Reverse complement")
print("5`-"+colored(DNAStr)+"-3`")
print("   "+''.join(['|'for c in range(len(DNAStr))]))
print("3`-"+colored(reverseComplement(DNAStr)[::-1])+"-5` Complement")
print("5`-"+colored(reverseComplement(DNAStr))+"-3` Rev Complement")
print("[5]GC Content")
print(GCcontent(DNAStr))
print("[6] GC content in subsection k=5")
print(gc_content_subsec(DNAStr,k=5))