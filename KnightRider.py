# This is my signature purple crown as seen on the PiCast Show
import time
import board
import neopixel 

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18
num_pixels = 256

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.3, auto_write=False, pixel_order=ORDER
)

RED = 0xff0000

x = 3
y = 4
for i in range(255):
    while x < 255 and y < 255:
        pixels[x] = RED
        pixels[y] = RED
        x += 8
        y =+ 8
pixels.show()
time.sleep(2)