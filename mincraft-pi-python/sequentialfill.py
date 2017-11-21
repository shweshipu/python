from initme import init
import time
mc = init()

## wayyyyyy to slow

def loop():
	i = 1
	lasttime=0
	x=-128
	y=-64
	z=-128
	while(True):
		now =time.time()
		if(now>lasttime+0):
			mc.setBlock(x,y,z,0)
			print(x)
			y+=1
			if(y>64):
				y=-64
			if(i%128==0):
				x+=1
				if(x>128):
					x=-128
			
			
			if(i%(256*128)==0):
				z+=1
				if(z>128):
					z=-128
			i+=1
			#lasttime=time.time()
def main():
	loop()
main()
