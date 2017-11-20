from initme import init
import time
mc = init()

x,y,z = mc.player.getPos()
def spin():
	i = 0
	lasttime=0
	blockid=0
	# stuff for keeping track of placed blocks
	blockids = []
	blockx=[]
	blocky=[]
	blockz=[]
	while(True):
		x,y,z = mc.player.getPos()
		now =time.time()
		if(now>lasttime+0.2):
			if(len(blockids)>12):
				#delete last block
				mc.setBlock(blockx[0],blocky[0],blockz[0],blockids[0])
				#delete oldest array entry
				del blockids[0]
				del blockx[0]
				del blocky[0]
				del blockz[0]
			#add the newest blocks coords and id
			blockx.append(x)
			blocky.append(y)
			blockz.append(z)
			if(mc.getBlock(x,y,z) != 89):
				blockids.append(mc.getBlock(x,y,z))
			#actually placing a block
			mc.setBlock(x,y,z,89)
			
			i+=1
			lasttime=time.time()
def main():
	spin()
main()
