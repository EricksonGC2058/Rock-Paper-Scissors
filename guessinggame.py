import random

mysteryNumber = random.randint(1, 100)
score = 0

while True:
	guess = int(input("Guess a number between 1 and 100: "))
	score += 1 # the same as score = score + 1
	if guess == mysteryNumber:
		print("You guessed correctly, you have been drafted to serve in the Vietnam War. Let's go kill some gooks!")
		break
	elif guess > mysteryNumber:
		print("Too high, you have dodged the draft.")
	else:
		print("Too low, you are now publicly ridiculed for being a draft dodger you coward.")

print("You took " + str(score) + " guesses")