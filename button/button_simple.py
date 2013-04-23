"""
author: matt venn
"""

#import the library
import RPIO

#gpio pin 4 is pin 7 on the p1 header
button_pin = 4

#set the pin to be high to start, low when pressed
RPIO.setup(button_pin,RPIO.IN, pull_up_down=RPIO.PUD_UP)

while True:
    if RPIO.input(button_pin) == False:
	print "button pressed"
