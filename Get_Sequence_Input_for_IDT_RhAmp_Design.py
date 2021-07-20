#!/usr/bin/python

# Get_Sequence_Input_for_IDT_RhAmp_Design.py 

# This script produces a fasta file in the format specified by IDT to create primers with RhAmp technology.
# It takes three arguments:
#   1 - Path for the reference genome fasta file
#   2 - Target site
#   3 - Two nucleotides specifying possible alleles at this site

# Example usage: python Get_Sequence_Input_for_IDT_RhAmp_Design.py SARS-CoV-2.fasta 23012 AG


import sys

ref_name = sys.argv[1]
site = int(sys.argv[2]) - 1
begin = site - 100
end = site + 100
mutation = sys.argv[3]
exchange = "[" + mutation[0] + "/" + mutation[1] + "]"



with open(ref_name) as f:
    lines = f.readlines()

ref = list(''.join(lines[1:]))
ref[site] = exchange
ref = ''.join(ref).replace('\n','')


if begin > 0 and end < len(ref):
    target = ref[begin:end]
    filename = "IDT_target." + str(site+1) + "." + mutation + ".txt"
    f = open(filename,"w")
    print(">IDT_Target",file=f)
    print(target,file=f)
    f.close()
    print("Target sequence is written to", filename)
else:
    print("The selected site is too close to the edge of sequence, please select a better target.")


