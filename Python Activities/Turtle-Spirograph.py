# Spirograph

from turtle import *


# Make a Polygon with (x) sides

def polygon(x):

	L = ['red','green','blue','orange','purple','red','blue','green','purple','red','orange','blue']

	angle = 360/x
	i=0

	while x>0:
		color(L[i])
		forward(75)
		left(angle)
		x=x-1
		i=i+1


# Make a Spirograph

def spirograph():
	
	while True:     # Infinite Loop
		polygon(8)
		left(5)     # Five degree shift


shape('turtle')
spirograph()
done()