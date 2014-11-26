import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

try:
    while True:
        #Get the block hit events
        blockHits = mc.events.pollBlockHits()
        # if a block has been hit
        if blockHits:
            # for each block that has been hit
            for blockHit in blockHits:
                #print (blockHit)
                print(blockHit.pos)
                block = mc.getBlockWithData(blockHit.pos.x, blockHit.pos.y, blockHit.pos.z)
                print (block)
        #sleep for a short time        
        time.sleep(0.1)
except KeyboardInterrupt:
    print("stopped")