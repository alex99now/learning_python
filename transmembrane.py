#!/usr/bin/env python3

import gzip
import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
#more functions
# average KD for 8mer score 
# function computing average KD score given peptide 
# need 20 elif statements using table  

def read_fasta(filename):
	name = None
	seqs = []
	
	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()

    
def getKD(seq):
    KD = 0  
    for aa in seq:
        if aa   == 'I': KD += 4.5
        elif aa == 'V': KD += 4.2
        elif aa == 'L': KD += 3.8
        elif aa == 'F': KD += 2.8
        elif aa == 'C': KD += 2.5
        elif aa == 'M': KD += 1.9
        elif aa == 'A': KD += 1.8
        elif aa == 'G': KD += -0.4
        elif aa == 'T': KD += -0.7
        elif aa == 'S': KD += -0.8
        elif aa == 'W': KD += -0.9
        elif aa == 'Y': KD += -1.3
        elif aa == 'P': KD += -1.6
        elif aa == 'H': KD += -3.2
        elif aa == 'E': KD += -3.5
        elif aa == 'Q': KD += -3.5
        elif aa == 'D': KD += -3.5
        elif aa == 'N': KD += -3.5
        elif aa == 'K': KD += -3.9
        elif aa == 'R': KD += -4.5
    return KD/len(seq)
   
def hydro(seq, threshold, kmer):
    for i in range(0, len(seq)-kmer +1):
        if getKD(seq[i:i+kmer]) > threshold and 'P' not in seq[i:i+kmer]:
            return True 
    return False 
           
for name, seq in read_fasta('proteins.fasta.gz'):
    if hydro(seq[0:30], 2.5, 8) and hydro(seq[30:], 2.0, 11):
        print(name)
          
       
"""


18w
Dtg
Krn
Lac
Mcr
PRY
Pxt
Pzl
QC
Ror
S1P
S2P
Spt
apn
bai
bdl
bou
bug
cue
drd
ft
grk
knk
ksh
m
nac
ort
rk
smo
thw
tsg
waw
zye
"""
