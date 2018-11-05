#!/usr/bin/env python36


def find(orderd_list, element_to_find):
	for element in orderd_list:
		if element == element_to_find:
			return True
	return False
		
		
if __name__ =="__main__":
	a_list = list(range(0,100,2))
	number = int(input("please enter a number: "))
	print(find(a_list, number))
