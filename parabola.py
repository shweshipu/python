from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

for i in range(-16,16):
	mc.setBlock(x+i,y,z+i**2,1)
