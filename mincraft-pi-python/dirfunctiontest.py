from initme import init
from direction import getMoveDir
mc = init()
x,y,z = getMoveDir(mc)
mc.setBlock(x,y,z,1)
