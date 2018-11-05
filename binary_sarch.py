#!/usr/bin/env python36

#homework
#lior cohen
#

def find(ordered_list, element_to_find):
	start_index = 0
	end_index = int(len(ordered_list)) -1
	
	while True:
		middle_index = int((start_index + end_index)/2)
		if middle_index == start_index or middle_index == end_index:
			if ordered_list[middle_index] == element_to_find:
				return True
			else:
				return False
	
		middle_element = middle_index
		if middle_element == element_to_find:
			return True
		elif element_to_find < middle_element:
			end_index = middle_index
		else:
			start_index = middle_index	

if __name__ == "__main__":
	a_list = list(range(1,100))
	num = int(input("please enter a number: "))
	var = find(a_list, num)
	print(var)
