#!/usr/bin/env python36

#####################
#
#
#
#
###################

import random

gen_number = random.randrange(1000, 9999)
number = str(gen_number)
cows_bulls = [0,0]
guess_number = 0
print("lets play a little game called cows and bulls")
print("you need to guess a 4 digts number")
print("for every correct number place you get a cow")
print("for every correct number in a worng palce you get bull")

while cows_bulls[0] < 4:
	guess = str(input("please enter a guess:  "))
	guess_number += 1
	cows_bulls = [0,0]
	if int(guess) < 1000 or int(guess) > 9999:
		print("you need to chose between 1000-9999")
	else:
		for i in range(4):
			if guess[i] == number[i]:
				cows_bulls[0] += 1
				cows_bulls[1] -= 1
		for j in range(4):
			if guess[j] in number:
				cows_bulls[1] += 1
			#	if cows_bulls[0] > 0 and cows_bulls[1] > 0: 
			#		cows_bulls[1] -= cows_bulls[0]
		print("you have {} cows and {} bulls".format(cows_bulls[0], cows_bulls[1]))
print("wowoooo you made it with {} guesses".format(guess_number))
print(number)
