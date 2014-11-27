import time
import mcpi.minecraft as minecraft
import mcpi.vec3 as vec3
from mcpi_pin import McPin


# The location of the pins for the seven segment display.
# YOU MUST EDIT THESE VALUES TO MATCH YOUR WORLD
a_loc = vec3.Vec3(80, 1, -183)
b_loc = vec3.Vec3(79, 1, -184)
c_loc = vec3.Vec3(78, 1, -183)
d_loc = vec3.Vec3(77, 1, -184)
e_loc = vec3.Vec3(76, 1, -183)
f_loc = vec3.Vec3(75, 1, -184)
g_loc = vec3.Vec3(74, 1, -183)


# The location of all the pixels used in the seven segment display.
# YOU MUST EDIT THESE VALUES TO MATCH YOUR WORLD
a_pixels = [vec3.Vec3(78, 9, -176),
            vec3.Vec3(77, 9, -176),
            vec3.Vec3(76, 9, -176)]

b_pixels = [vec3.Vec3(75,8,-176),
            vec3.Vec3(75,7,-176),
            vec3.Vec3(75,6,-176)]

c_pixels = [vec3.Vec3(75,4,-176),
            vec3.Vec3(75,3,-176),
            vec3.Vec3(75,2,-176)]

d_pixels = [vec3.Vec3(78, 1, -176),
            vec3.Vec3(77, 1, -176),
            vec3.Vec3(76, 1, -176)]

e_pixels = [vec3.Vec3(79,4,-176),
            vec3.Vec3(79,3,-176),
            vec3.Vec3(79,2,-176)]

f_pixels = [vec3.Vec3(79,8,-176),
            vec3.Vec3(79,7,-176),
            vec3.Vec3(79,6,-176)]

g_pixels = [vec3.Vec3(78, 5, -176),
            vec3.Vec3(77, 5, -176),
            vec3.Vec3(76, 5, -176)]

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