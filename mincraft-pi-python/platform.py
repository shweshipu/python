from initme import init
import math
import time
mc = init()

x,y,z = mc.player.getPos()
a = 0
b = 0
c = 0
def plat(a,b,c):
	i = 0
	lasttime=0
	blockid=0
	while(True):
		x,y,z = mc.player.getPos()
		now =time.time()
		if(now>lasttime+0.2):
			#place a new block
			mc.setBlock(x+dx,y,z+dz,89)
			#delete last block
			if(blockid!=89):
				mc.setBlock(a,b,c,blockid)
			#record block
			a = x+dx
			b = y
			c = z+dz
			blockid=mc.getBlock(a,b,c)
			#increment
			i+=1
			lasttime=time.time()
def main(a,b,c):
	plat(a,b,c)
main(a,b,c)
