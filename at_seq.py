#!/usr/bin/env python3

import random
random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

length = 30
dna = ''
at_count = 0
alphabet = 'AAAAAACGT'
for i in range(length):
    nt = random.choice(alphabet)
    if nt == 'A' or nt == 'T': at_count += 1
    dna += nt
"""
    if r < 0.35:
    elif r < 0.65:
    elif r < 0.8:
    else:
    
    if r < 0.6:
        r = random.randint(0, 1)
        if r == 0: dna += 'A'
        else:      dna += 'T'
        at_count += 1
    else:
        r = random.randint(0, 1)
        if r == 0: dna += 'C'
        else:      dna += 'G'
"""
print(length, at_count / length, dna)


"""
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
