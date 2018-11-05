#!/usr/bin/env python36


def list_append(list_to_append, data_for_the_list):
	list_to_append.append(data_for_the_list)
	return list_to_append

lst=[]

list_length=int(input("please enter the list length: "))
type(list_length)
i=0
for i in range(list_length):
	data_for_list=input("please enter a number:")
	list_append(lst,data_for_list)
	print(lst)
