from initme import init
mc=init()

x,y,z = mc.player.getPos()

for i in range(-5,5):
	r=5
	h=int(((i-x)**2+r**2)**1/2)+z
	mc.setBlocks(x,y,h,x,y,z,17)
