def getMoveDir(mc):
	"""
	* make sure to put in mc as the mc = Minecraft.create thing
	* only does x and  z coords
	* you can multiply your x and z coords, default is 15,
	this increases the distance from you
	"""
	x,y,z = mc.player.getPos()
	a,b,c =  mc.player.getPos()
	while(int(x)+int(z)==int(a)+int(c)):
		a,b,c =  mc.player.getPos()
	x+=(int(a)-int(x))*15
	z+=(int(c)-int(z))*15
	return(x,y,z)
