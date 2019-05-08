import time
import machine
import neopixel

num_pixel = 10 
pixels = neopixel.NeoPixel(machine.Pin(14), num_pixel)
pixels.fill((0, 0, 0))
pixels.write()
 
"""
Space stone- Blue (38,110,246)
Power stone- Purple (228,41,242)
Soul stone- Orange (255,139,0)
Reality stone- Red (255,1,48)
Mind stone- Yellow (255,211,0)
Time stone- Green (18,231,114)

infinity_color = {
    'soul' : (255,139,0),
    'reality': (255,1,48),
    'space' : (38,110,246),
    'power' : (228,41,242),
    'time' : (18,231,114),
    'mind' : (255,211,0),
}

infinity_stone = {
    0 : (255,139,0),
    1 : (255,1,48),
    2 : (38,110,246),
    3 : (228,41,242),
    4 : (18,231,114),
    5 : (255,211,0),
}

Expected combination in one cycle:
8,9,0,1,2,5
9,0,1,2,3,6
0,1,2,3,4,7
1,2,3,4,5,8
2,3,4,5,6,9
3,4,5,6,7,0
4,5,6,7,8,1
5,6,7,8,9,2
6,7,8,9,0,3
7,8,9,0,1,4
"""

def infinity_loop(num_pixel, wait):
    pos_init = (8, 9, 0, 1, 2, 5)
    num_pixel = 10
    pixel_loop = list(range(num_pixel))

    infinity_stone = {
        0: (255, 139, 0),
        1: (255, 1, 48),
        2: (38, 110, 246),
        3: (228, 41, 242),
        4: (18, 231, 114),
        5: (255, 211, 0),
    }

    for i in range(0, num_pixel):
        loop = list(range(num_pixel))
        for j, pos in enumerate(pos_init):
            pos += i
            if pos >= num_pixel:
                pos = pos - num_pixel
            loop[pos] = infinity_stone.get(j)
        pixel_loop[i] = loop

    if pixel_loop:
        for pixel in pixel_loop:
            pixels.fill((0,0,0))
            pixels.write()
            for k, pixel_color in enumerate(pixel):
                if type(pixel_color) is tuple:
                    pixels[k] = pixel_color
                    pixels.write()
            time.sleep(wait)

while True:
    infinity_loop(10, 1)
