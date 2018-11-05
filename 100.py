#!/usr/bin/env python36

#####
#name: lior cohen
#date: 11/6/18
#description: get a name and age from the user and tell 
#them the year they will turn 100 years old
####

name = str(input("please entar your name: "))
age = int(input("please enter yout age:  "))
year = (str((2018 - age) +100))

print("{}, will be 100 years old in the year {}".format(name, year))
