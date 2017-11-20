from initme import init
mc=init()

x,y,z = mc.player.getPos()
 #eh
for i in range(0,10000):
		#stairwell
		dx=0.0
		dz=0.0
		dx=math.sin((float(i))*math.pi/100)
		dz=math.cos((float(i))*math.pi/100)
		if(dx<0.1 and dx>-0.1):
			dx=0
		if(dz<0.1 and dz>-0.1):
			dz=0
		try:
			dx/=abs(dx)
			dz/=abs(dz)
		except ZeroDivisionError:
			pass
	
		mc.setBlock(x+dx,y,z+dz,4)
