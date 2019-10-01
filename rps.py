# Garrett Erickson
# Rock, Paper, Scissors!
# rps.py
# added comment for github
import random
pScore = 0
cScore = 0
ties = 0
cMoves = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")
pName = input("What is your name? ")

def printscore():
	print("Score: ")
	print(pName + ": " + str(pScore))
	print("Computer: " + str(cScore))
	print("Ties: " + str(ties))

while True:
	pMove = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors, or 'q' to quit")
# (r, p, s, q)
	printScore()
# check if q is entered if so end game
	if pMove == 'q':
		break
# put a computer move (random)
	cMove = random.choice(cMoves)
# compare player move with the computer move
# player picks rock
	if pMove == "r":
		print(pName + " picked Rock!")
		if cMove == "rock":
			print("Computer picks Rock!")
			print("Tie")
			ties += 1
		elif cMove == "paper":
			print("Computer picks Paper!")
			print("Oh no! Paper covers Rock!")
			cScore += 1
		else cMove == "scissors":
			print("Computer picks Scissors!")
			print("Yes! Rock breaks Scissors!")
			pScore += 1
# player picks paper
	elif pMove == "p":
		print(pName + " picked Paper!")
		if cMove == "rock":
			print("Computer picks Rock!")
			print("Awesome! Paper covers Rock!")
			pScore += 1
		elif cMove == "paper":
			print("Computer picks Paper!")
			print("Tie")
			ties += 1
		else cMove == "scissors":
			print("Computer picks Scissors!")
			print("Dammit... Scissors cuts Paper!")
			cScore += 1
# player picks scissors
	elif pMove == "s":
		print(pName + " picked Scissors!")
		if cMove == "rock":
			print("Computer picks Rock!")
			print("No! Rock breaks Scissors!")
			cScore += 1
		elif cMove == "paper":
			print("Computer picks Paper!")
			print("Nice one! Scissors cut Paper!")
			pScore += 1
		else cMove == "scissors":
			print("Computer picks Scissors!")
			print("Tie")
			ties += 1
# check if pMove is valid
	else:
		print("That is not an option")