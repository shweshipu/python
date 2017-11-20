from initme import init
from shapes import sphere
mc = init()
x,y,z = mc.player.getPos()
sphere(mc,x,y,z,5,5,5,89)
sphere(mc,x,y,z,4,4,4,0)
