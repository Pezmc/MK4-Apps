___name___         = "Flash Colours"
___license___      = "MIT"
___categories___   = ["Homescreens"]
___dependencies___ = ["homescreen", "shared/logo.png"]
___launchable___   = False
___bootstrapped___ = True

import ugfx
from homescreen import *
import time

# Background stuff
init()
ugfx.clear(ugfx.html_color(0x000000))

colours = [
    ugfx.html_color(0xFF0000),
    ugfx.html_color(0x00FF00),
    ugfx.html_color(0x0000FF)
]

index = 0
colourCount = len(colours)
while True:
    ugfx.clear(colours[index % colourCount])
    sleep_or_exit(1)
    index += 1
