#!/usr/bin/env python36

#name: lior
#date: 23/05/18
import sys

print(sys.version)

file=open('test.txt','w')
file.write(input("what is yout name? \n") + "\n")
file.write(input("how old are you?") + "\n")
file.write("you think this is funny? " + input("you think this is funny? ") + "\n")

file.close()
