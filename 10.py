#!/usr/bin/env python36

##################
#name: lior cohen
#date: 13/6/18
#decription:
##################

number = int(input("please enter a number to test: "))

a_list = range(1, number + 1)

for i in a_list:
	if number % i == 0:
		print(i)
		
