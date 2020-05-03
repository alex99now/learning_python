#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'
step = 3

for i in range(0, len(dna) -step + 1, step):
    print(dna[i:i+step])

"""
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
