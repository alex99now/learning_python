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

#calculate mean
sum = 0
for n in data:
    sum += n
mean = sum/c 

#calculate std dev
sum = 0
for i in data:
    sum += (i - mean) **2
stddev = sqrt(sum/c)


print('Count: {}'.format(len(data)))
print('Minimum: {}'.format(data[0]))
print('Maximum: {}'.format(data[-1]))
print('Mean:', '%.5f' % mean)
print('Std. dev:', '%.5f' % stddev)
print('Median: {:.5f}'.format((data[4] + data[5])/ 2))


"""
python3 stats.py numbers.txt
Count: 10
Minimum: -1.0
Maximum: 256.0
Mean: 29.147789999999997
Std. dev: 75.777
Median 2.35914
"""
