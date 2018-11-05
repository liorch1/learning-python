#!/usr/bin/env python36

############
#
#
#dictinary 

with open('Training_01.txt', 'r') as f:
	line = f.readline()
	counter = {}
	while line:
		line = line[3:-26]
		if line in counter:
			counter[line] += 1
		else:
			counter[line] = 1
		line = f.readline()
				
print(counter)

