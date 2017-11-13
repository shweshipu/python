from initme import init
import math
mc = init()

x,y,z = mc.player.getPos()

#remember to push to github
for i in range(-5,5):
	#the outer structure
	if(i<0 and i!=-5):
		mc.setBlocks(x+i,y-i**2,z+i,x+i,y-(i-1)**2,z+i,17)
		mc.setBlocks(x-i,y-i**2,z+i,x-i,y-(i-1)**2,z+i,17)
	if(i>0):
		mc.setBlocks(x+i,y-i**2,z+i,x+i,y-(i+1)**2,z+i,17)
		mc.setBlocks(x-i,y-i**2,z+i,x-i,y-(i+1)**2,z+i,17)
	mc.setBlocks(x+i,y-i**2,z+i,x-i,y-i**2,z-i,5)
	if(i==0):
		mc.setBlock(x,y,z,89)
for i in range(9,25):
	#stairwell
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
	
	mc.setBlock(x+dx,y-i,z+dz,4)
	mc.setBlocks(x+dx,y-i+1,z+dz,x+dx,y-i+3,z+dz,0)
