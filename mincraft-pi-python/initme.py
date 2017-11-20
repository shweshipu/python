from mcpi.minecraft import Minecraft
from mcpi import block

def init():
    #127.0.0.1 for localhost , 10.183.13.13 for coleman 192.168.3.5 tristhtthtm
    mc = Minecraft.create("127.0.0.1",4711)

    return(mc)
