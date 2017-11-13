from initme import init
mc = init()
                                            
x, y, z = mc.player.getPos()  
mc.setBlocks(-128,-64,-128,128,64,128,0)
mc.setBlock(0,32,0)
