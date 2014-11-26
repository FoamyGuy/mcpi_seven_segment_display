import time

import mcpi.minecraft as minecraft
import mcpi.vec3 as vec3

from mcpi_pin import McPin


# The location of the pins for the seven segment display.
# YOU MUST EDIT THESE VALUES TO MATCH YOUR WORLD
a_loc = vec3.Vec3(108,1,-137)
b_loc = vec3.Vec3(107,1,-138)
c_loc = vec3.Vec3(106,1,-137)
d_loc = vec3.Vec3(105,1,-138)
e_loc = vec3.Vec3(104,1,-137)
f_loc = vec3.Vec3(103,1,-138)
g_loc = vec3.Vec3(102,1,-137)


# The location of all the pixels used in the seven segment display.
# YOU MUST EDIT THESE VALUES TO MATCH YOUR WORLD
a_pixels = [vec3.Vec3(106,9,-130),
            vec3.Vec3(105,9,-130),
            vec3.Vec3(104,9,-130)]

b_pixels = [vec3.Vec3(103,8,-130),
            vec3.Vec3(103,7,-130),
            vec3.Vec3(103,6,-130)]

c_pixels = [vec3.Vec3(103,4,-130),
            vec3.Vec3(103,3,-130),
            vec3.Vec3(103,2,-130)]

d_pixels = [vec3.Vec3(104,1,-130),
            vec3.Vec3(105,1,-130),
            vec3.Vec3(106,1,-130)]

e_pixels = [vec3.Vec3(107,2,-130),
            vec3.Vec3(107,3,-130),
            vec3.Vec3(107,4,-130)]

f_pixels = [vec3.Vec3(107,6,-130),
            vec3.Vec3(107,7,-130),
            vec3.Vec3(107,8,-130)]

g_pixels = [vec3.Vec3(106,5,-130),
            vec3.Vec3(105,5,-130),
            vec3.Vec3(104,5,-130)]

if __name__ == "__main__":

    old_val = 0

    # Create mc object.
    mc = minecraft.Minecraft.create()

    a_pin = McPin(mc, 'a', 1, a_loc)
    b_pin = McPin(mc, 'b', 1, b_loc)
    c_pin = McPin(mc, 'c', 1, c_loc)
    d_pin = McPin(mc, 'd', 1, d_loc)
    e_pin = McPin(mc, 'e', 1, e_loc)
    f_pin = McPin(mc, 'f', 1, f_loc)
    g_pin = McPin(mc, 'g', 1, g_loc)

    while 1:

        out_str = ""
        out_str += str(a_pin.read_pin())
        out_str += str(b_pin.read_pin())
        out_str += str(c_pin.read_pin())
        out_str += str(d_pin.read_pin())
        out_str += str(e_pin.read_pin())
        out_str += str(f_pin.read_pin())
        out_str += str(g_pin.read_pin())

        print(out_str)

        if a_pin.read_pin():
            for pixel in a_pixels:
                mc.setBlock(pixel, 57)
        else:
            for pixel in a_pixels:
                mc.setBlock(pixel, 49)

        if b_pin.read_pin():
            for pixel in b_pixels:
                mc.setBlock(pixel, 57)
        else:
            for pixel in b_pixels:
                mc.setBlock(pixel, 49)

        if c_pin.read_pin():
            for pixel in c_pixels:
                mc.setBlock(pixel, 57)
        else:
            for pixel in c_pixels:
                mc.setBlock(pixel, 49)

        if d_pin.read_pin():
            for pixel in d_pixels:
                mc.setBlock(pixel, 57)
        else:
            for pixel in d_pixels:
                mc.setBlock(pixel, 49)

        if e_pin.read_pin():
            for pixel in e_pixels:
                mc.setBlock(pixel, 57)
        else:
            for pixel in e_pixels:
                mc.setBlock(pixel, 49)

        if f_pin.read_pin():
            for pixel in f_pixels:
                mc.setBlock(pixel, 57)
        else:
            for pixel in f_pixels:
                mc.setBlock(pixel, 49)

        if g_pin.read_pin():
            for pixel in g_pixels:
                mc.setBlock(pixel, 57)
        else:
            for pixel in g_pixels:
                mc.setBlock(pixel, 49)

        time.sleep(.3)