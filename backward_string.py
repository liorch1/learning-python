#!/usr/bin/env python36


##########################
#name:lior cohen
#date: 10/06/18
#decription: get a lonf string and print it backwards
#########################

enter_string = input("please enter a long strind: ")

def string_backwards(enter_string):
	list_words = enter_string.split()
	return "{}".format(" ".join(list_words[::-1]))

var = string_backwards(enter_string)
print(var)
