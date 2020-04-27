#!/usr/bin/env python3

from math import sqrt
import fileinput

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import any other modules!


data = []
for line in fileinput.input():
	if line.startswith('#'): continue 
	line = line.rstrip() 
	data.append(float(line)) 
data.sort()

c = len(data)
m = (data[0] + data[1] + data[2] + data[3] + data[4] + data[5] + data[6] + data[7] + data[8] + data[9]) / 10
n1 = (data[0] - m)**2
n2 = (data[1] - m)**2
n3 = (data[2] - m)**2
n4 = (data[3] - m)**2
n5 = (data[4] - m)**2
n6 = (data[5] - m)**2
n7 = (data[6] - m)**2
n8 = (data[7] - m)**2
n9 = (data[8] - m)**2
n10 = (data[9] - m)**2
e = (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10)
n = e / c
stddev = sqrt(n)

print('Count: {}' .format(len(data)))
print('Minimum: {}' .format(data[0]))
print('Maximum: {}' .format(data[-1]))
print('Mean:', m)
print('Std. dev:', '%.5g' % stddev)
print('Median: {}' .format((data[4] + data[5])/ 2))




"""
python3 stats.py numbers.txt
Count: 10
Minimum: -1.0
Maximum: 256.0
Mean: 29.147789999999997
Std. dev: 75.777
Median 2.35914
"""
