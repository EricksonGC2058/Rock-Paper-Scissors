from turtle import *

racism = Turtle()
screen = racism.getscreen()

racism.forward(50)

def writeName():
	name = screen.textinput("name box", "What is your name?")
	racism.write(name, move=True, align="left", font=("Comic Sans MS",30,"normal"))
	screen.listen()

screen.onkey(writeName, "w")

screen.listen()

screen.mainloop()