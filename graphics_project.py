from graphics import *
from random import randint
win = GraphWin("PLOT RANDOM", 400, 400)
count = 0
while True:
	x = randint(0,400)
	y = randint(0,400)
	pt = Point(x, y)
	pt.setFill("red")
	pt.draw(win)
	count = count = 1	
input("Press return to end")

win.close()
