#!/usr/bin/env python36

import random

a_list = []
b_list = []
c_list = [] #list after filtering
list_element = int(input("please enter a number: "))

for i in range(list_element+1):
	a_list.append(random.randrange(1,100,1))
	
for j in range(11):
	b_list.append(random.randrange(1,100,1))

for num in a_list:
	if num in b_list and num not in c_list:
		c_list.append(num)
	
print(c_list)
