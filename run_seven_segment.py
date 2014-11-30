import time
import mcpi.minecraft as minecraft
import mcpi.vec3 as vec3
from mcpi_pin import McPin


# The location of the pins for the seven segment display.
# YOU MUST EDIT THESE VALUES TO MATCH YOUR WORLD
a_loc = minecraft.Vec3(230,1,-308)
b_loc = minecraft.Vec3(229,1,-309)
c_loc = minecraft.Vec3(228,1,-308)
d_loc = minecraft.Vec3(227,1,-309)
e_loc = minecraft.Vec3(226,1,-308)
f_loc = minecraft.Vec3(225,1,-309)
g_loc = minecraft.Vec3(224,1,-308)


# The location of all the pixels used in the seven segment display.
# YOU MUST EDIT THESE VALUES TO MATCH YOUR WORLD
a_pixels = [minecraft.Vec3(228,9,-301),
            minecraft.Vec3(227,9,-301),
            minecraft.Vec3(226,9,-301)]

b_pixels = [minecraft.Vec3(225,8,-301),
            minecraft.Vec3(225,7,-301),
            minecraft.Vec3(225,6,-301)]

c_pixels = [minecraft.Vec3(225,4,-301),
            minecraft.Vec3(225,3,-301),
            minecraft.Vec3(225,2,-301)]

d_pixels = [minecraft.Vec3(228,1,-301),
            minecraft.Vec3(227,1,-301),
            minecraft.Vec3(226,1,-301)]

e_pixels = [minecraft.Vec3(229,4,-301),
            minecraft.Vec3(229,3,-301),
            minecraft.Vec3(229,2,-301)]

f_pixels = [minecraft.Vec3(229,8,-301),
            minecraft.Vec3(229,7,-301),
            minecraft.Vec3(229,6,-301)]

g_pixels = [minecraft.Vec3(228,5,-301),
            minecraft.Vec3(227,5,-301),
            minecraft.Vec3(226,5,-301)]

if __name__ == "__main__":

    # Create mc object.
    mc = minecraft.Minecraft.create()

    a_pin = McPin(mc, 'a', 1, a_loc)
    b_pin = McPin(mc, 'b', 1, b_loc)
    c_pin = McPin(mc, 'c', 1, c_loc)
    d_pin = McPin(mc, 'd', 1, d_loc)
    e_pin = McPin(mc, 'e', 1, e_loc)
    f_pin = McPin(mc, 'f', 1, f_loc)
    g_pin = McPin(mc, 'g', 1, g_loc)

    while True:

        """
        out_str = ""
        out_str += str(a_pin.read_pin())
        out_str += str(b_pin.read_pin())
        out_str += str(c_pin.read_pin())
        out_str += str(d_pin.read_pin())
        out_str += str(e_pin.read_pin())
        out_str += str(f_pin.read_pin())
        out_str += str(g_pin.read_pin())
        print(out_str)
        """

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