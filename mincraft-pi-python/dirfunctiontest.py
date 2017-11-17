from initme import init
from direction import getmovedir
mc = init()
x,y,z = getmovedir(mc)
mc.setBlock(x,y,z,1)
