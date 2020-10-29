from graphics import *

def lastbit():
	return "44"

def main():

	win = GraphWin("Some Basic GUI Examples", 700, 500)   #title, width, height
	win.setBackground("white")


	apoint = Point(45, 80)
	anotherpoint = Point(500, 300)
	apoint.draw(win)
	anotherpoint.draw(win)


	myline = Line(apoint, anotherpoint)
	myline.setArrow("last")   # options: first, last, both, none
	myline.draw(win)


	mycircle = Circle(anotherpoint, 75)    # centerpoint, radius
	mycircle.draw(win)


	myrect = Rectangle(Point(10,10), Point(80,80))    # upper-left, bottom-right
	myrect.draw(win)


	mylabel = Text(Point(450, 80), "Hello GUI world!")    # anchorpoint (centered), text_string
	mylabel.setSize(24)
	mylabel.setFace("courier")
	mylabel.setStyle("bold italic")
	mylabel.setTextColor("red")
	mylabel.draw(win)


	textbox1 = Entry(Point(150, 425), 15)    # centerpoint, width
	textbox1.setTextColor("white")
	textbox1.setFill("green")
	textbox1.draw(win)


	# Must be a GIF!
	myimage = Image(Point(45, 45), "rob_headshot.gif")    # anchorpoint, filename
	myimage.draw(win)


	# Get the user's input from the textbox and display it in the label

	win.getMouse()   # pause for click in window
	userinput = textbox1.getText()
	mylabel.undraw()
	t2 = Text(Point(450, 80), "Welcome, " + userinput )
	t2.setSize(24)
	t2.setFace("courier")
	t2.setStyle("bold italic")
	t2.setTextColor("red")
	t2.draw(win)

	# Practice executing a function
	win.getMouse()   # pause for click in window
	t2.undraw()
	myNumber = lastbit()
	t3 = Text(Point(450, 80), "Favorite number: " + myNumber )
	t3.setSize(24)
	t3.setFace("courier")
	t3.setStyle("bold italic")
	t3.setTextColor("red")
	t3.draw(win)




	win.getMouse()   # pause for click in window
	win.close()


main()