#!/usr/bin/env python36

####
#name: lior
#date: 6/3/18
##description: Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
#			   and makes a new list of only the first and last elements of the given list.
# 			   For practice, write this code inside a function.
####


def list_start_end(x_list):
	return [x_list[0], x_list[len(x_list)-1]]
	
#function check 
var = [1,2,3,4,5,6,76,7]

var = list_start_end(var)
print(var) #[1,7]
