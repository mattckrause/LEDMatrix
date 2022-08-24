import time
import board
import neopixel

pixel_pin = board.D18
num_pixels = 256
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
	pixel_pin, num_pixels, brightness=0.3, auto_write=False, pixel_order=ORDER
)

pixels[8] = 0xff0000
pixels.show()
time.sleep(2)
