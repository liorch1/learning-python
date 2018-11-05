#!/usr/bin/env python36

#####
#date: 11/6/18
#lior cohen
# list less than the user input.
#####
a_list = [1,2,4,22,25,6,4,2,7,14,2341,123,434]
number = int(input("please enter a number: "))
a_list2 = []
for i in a_list:
	if i <= number:
		a_list2.append(i)
print(a_list2)		
