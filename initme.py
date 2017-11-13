from mcpi.minecraft import Minecraft
from mcpi import block

def init():
    
    mc = Minecraft.create("127.0.0.1",4711)

    return(mc)