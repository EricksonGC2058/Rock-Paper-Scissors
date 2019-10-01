#Conditional
print("Welcome to Ticket Box")
print("You must be at least 18 to see an r rated movie")
age = int(input("How old are you? "))

if age > 17:
	print("You can go see an R rated movie")
else:
	print("You cannot go see an R rated movie")

print("Fuck you")

mysteryNum = 6
guess = int(input("Guess a number between 1 and 10: "))

if guess == mysteryNum:
	print("Fuck you. Fuck you. You got it. Fuck. You outsmarted a fucking computer. What the fuck.")
elif guess > 10:
	print("we only fuckin 10 year olds or younger jackass")
elif guess > mysteryNum:
	print("B   r   u   h     niggapoop")
else:
	print("Certified Hood Classic")

# conditional operators: >, <, >=, <=, == (is equal to), != (is not equal to)

birthday = input("Is today your birthday(yes/no): ")
if birthday == "yes":
	print("You still fucking suck.")
elif birthday =="no":
	print("You fucking suck.")
else:
	print("You really fucking stink. Like, really really fucking stink.")