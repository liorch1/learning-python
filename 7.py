#!/usr/bin/env python36

#####################
#
#
#
#
###################

string = str(input("please enter a word: "))

string_backwards = string[::-1]


print(string)
print(string_backwards)
if string == string_backwards:
	print("sring match")
else:
	print("not match")
