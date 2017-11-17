from initme import init
import math
import time
mc = init()

x,y,z = mc.player.getPos()
a = 0
b = 0
c = 0
def spin(a,b,c):
	i = 0
	lasttime=0
	blockid=0
	while(True):
		x,y,z = mc.player.getPos()
		now =time.time()
		if(now>lasttime+0.2):
			dx=0.0
			dz=0.0
			dx=math.sin((float(i%8))*math.pi/4)
			dz=math.cos((float(i%8))*math.pi/4)
			if(dx<0.1 and dx>-0.1):
				dx=0
			if(dz<0.1 and dz>-0.1):
				dz=0
			try:
				dx/=abs(dx)
				dz/=abs(dz)
			except ZeroDivisionError:
				pass
			#delete last block
			######mc.setBlocks(x+1,y,z+1,x-1,y+3,z-1,0)
			
			mc.setBlock(a,b,c,blockid)
			
			a = x+dx
			b = y
			c = z+dz
			blockid=mc.getBlock(a,b,c)
			mc.setBlock(a,b,c,89)
			#place a new block
			#setblock position
			
			i+=1
			lasttime=time.time()
def main(a,b,c):
	spin(a,b,c)
main(a,b,c)
