from graphics import *
import random

win = GraphWin("Coin Flipper Program!", 500, 500)
win.setBackground("pink")

t = Text(Point(250, 100), "Heads or Tails?")
t.setSize(30)
t.draw(win)

e = Entry(Point(250, 150), 15)
e.draw(win)

m = win.getMouse()
user_choice = e.getText()
if user_choice == "":
	user_choice = "Tails"
elif user_choice == "Heads":
	user_choice = "Heads"
else:
	user_choice == "Tails"

t.undraw()
e.undraw()


# Show what the user chose
t2 = Text(Point(250, 100), "You chose: " + user_choice)
t2.draw(win)
t3 = Text(Point(250, 175), "Click to flip!")
t3.draw(win)

win.getMouse()

# Flip the coin!
ch = random.choice(["Heads", "Tails"])
imh = Image(Point(250, 250), "h.gif")
imt = Image(Point(250, 250), "t.gif")

t3.undraw()

if ch == user_choice:
	t4 = Text(Point(250, 450), "You Win!")
	t4.draw(win)
else:
	t5 = Text(Point(250, 450), "You Lose!")
	t5.draw(win)


if ch == "Heads":
	imh.draw(win)
else:
	imt.draw(win)




win.getMouse()
win.close()