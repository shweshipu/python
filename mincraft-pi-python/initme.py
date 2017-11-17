from mcpi.minecraft import Minecraft
from mcpi import block

def init():
    #127.0.0.1 for localhost , 10.183.13.13 for coleman
    mc = Minecraft.create("10.183.4.139",4711)

    return(mc)
