"""
 This is a slightly modified version of print3D.py which is

 From the book: "Adventures in Minecraft"
 written by David Whale and Martin O'Hanlon, Wiley, 2014
 http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html

 This program reads from a CSV file and builds blocks in the
 Minecraft world. It will use the block where the player
 left clicks as the origin point for printing the data file.
"""


import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Create a constant for the name of your data file
# This makes it easier to use a different file in the future
FILENAME = "seven_segment.csv"

# Define a function that will print the contents of any file
# at any x,y,z coordinate in the Minecraft world
# filename - is the name of the file to open
# x,y,z - these are the coordinates of the origin (bottom corner)
def print3D(filename, originx, originy, originz):
  # Open the data file in read mode
  f = open(filename, "r")
  
  # Read all lines from the file into a 'lines' list variable
  lines = f.readlines()

  # The first line in the file is the metadata, it holds the 3 sizes
  # Split this line into parts, and set 3 variables, one for each size
  coords = lines[0].split(",")
  sizex = int(coords[0])
  sizey = int(coords[1])
  sizez = int(coords[2])

  # Use the 'lineidx' variable to keep track of the line number
  # in the loop below. Each time arount the loop, this will set to
  # the next line number, so that your loop processes one line at a time
  lineidx = 1
  
  # This first for loop reads through each vertical layer of the file
  for y in range(sizey):
    mc.postToChat(str(y)) # just so you can see what it is doing
    
    # Advance to the next line index
    lineidx = lineidx + 1
    
    # This inner loop reads through each east/west position in a line
    for x in range(sizex):
      # Get the whole line at this 'lineidx'
      line = lines[lineidx]
      
      # Advance to the next line index
      lineidx = lineidx + 1
      
      # Split this line into separate cells, at each comma
      data = line.split(",")
      
      # This (third) inner loop reads through each north/south position
      for z in range(sizez):
        # Get the blockid from the line at this z position
        # Convert it to a number by using int()
        blockid = int(data[z])
        # Build the block at the correct x,y,z position
        mc.setBlock(originx+x, originy+y, originz+z, blockid)


if __name__ == "__main__":
    try:
        while True:
            #Get the block hit events
            blockHits = mc.events.pollBlockHits()
            # if a block has been hit
            if blockHits:
                print3D("seven_segment.csv", blockHits[0].pos.x, blockHits[0].pos.y, blockHits[0].pos.z)
                break
            #sleep for a short time
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("stopped")