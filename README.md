mcpi_seven_segment_display
==========================
This project will show you how to create a virtual seven segment display inside of minecraft.

###[Walkthrough Video](http://youtu.be/uBwxMlkVlZc)

check_block_hit.py
------------------
A helper script used to find locations and block types inside of the Minecraft world.

mcpi_pin.py
-----------
Contains the McPin class which we will use to interface the python code with redstone circuts inside the game.

print_seven_segment.py
----------------------
Will print the Seven Segment Display for you instead of having to build it manually. Prints from seven_segment.csv

run_seven_segment.py
--------------------
The main script that drives the display. You must set the locations inside the script to valid locations from your own world. Once you have it will listen for the redstone pins to change value and will update the segments on the display accordingly.

