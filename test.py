import time
from rpi_ws281x import *

# LED Configuration
LED_Count      = 256
LED_PIN        = 18 #GPIO PIN 18 uses PWM!
LED_Freq_HZ    = 800000 #LED Signal frequency in hertz
LED_DMA        = 10
LED_Brightness = 10 #0 for dimmest, 225 for brightest
LED_Invert     = False
LED_Channel    = 0

strip = PixelStrip(LED_Count, LED_PIN, LED_Freq_HZ, LED_DMA, LED_Invert, LED_Brightness, LED_Channel)
strip.begin()

#Define test function (show color across matrix)
def wheel(pos):
	"""Generate rainbow colors across 0-255 positions"""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos <170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def colorWipe(stip, color, wait_ms=50):
	"""Wipe color across display 1 led at a time"""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i,color)
		strip.show()
		time.sleep(wait_ms/150000.0)

def rainbow(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/15000.0)

#Main program

rainbow(strip)
colorWipe(strip, Color(255, 0, 0))
colorWipe(strip, Color(0, 255, 0))
colorWipe(strip, Color(0, 0, 255))
colorWipe(strip, Color(0, 0, 0))

