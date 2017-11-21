from initme import init
import math
import random
mc = init()

while(True):
	x=random.randint(-128,128)
	z=random.randint(-128,128)
	y=random.randint(-64,64)
	mc.setBlock(x,y,z,0)
