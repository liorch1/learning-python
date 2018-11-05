#!/usr/bin/env python36

#homework
#lior cohen
#

def compare_answers(u1, u2):
	if u1 == u2:
		print("it's a tie")
	elif u1 == "rock":
		if u2 == "scissors":
			print("user 1 wins")
		else:
			print("user 2 wins")
	elif u1 == "paper":
		if u2 == "scissors":
			print("user 1 wins")
		else:
			print("user 2 wins")
	elif u1 == "scissors":
		if u2 == "paper":
			print("user 1 wins")
		else:
			print("user 2 wins")
	else:
		print("invalid choise! try again")

while True:
	user1 = str(input("please choose rock, paper or scissors: ")) 
	user2 = str(input("please choose rock, paper or scissors: "))
	compare_answers(user1 , user2)
	game = str(input("press enter to continue or type quit "))
	if game == "quit":
		break
