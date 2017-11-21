from initme import init
import math
mc = init()
# make the center
x,y,z = mc.player.getPos()
y-=1

mc.setBlocks(x-1,y,z-1,x+1,y,z+1,42)

# a 3*3 grid of booleans
col=[[False]*3]*3


dx=-1
dz=-1

while(True):
	for i in range (1,10):
		if(mc.getBlock(x+dx,y,z+dz)!=0):
			col[i-1][(i-1)%3]=True
		dx+=1
		if(dx>1):
			dx=-1
		if(i%3==0):
			dz+=1
			if(dz>1):
				dz=-1
	
