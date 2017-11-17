from initme import init
mc=init()

x,y,z = mc.player.getPos()
a,b,c =  mc.player.getPos()
while(int(x)+int(z)==int(a)+int(c)):
	a,b,c =  mc.player.getPos()
x+=(int(a)-int(x))*15
z+=(int(c)-int(z))*15
mc.setBlock(x,y,z,1)
