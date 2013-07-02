"""
author: matt venn
"""

#import the library
import RPIO
RPIO.setmode(RPIO.BOARD)

button_pin = 7

#set the pin to be high to start, low when pressed
RPIO.setup(button_pin,RPIO.IN, pull_up_down=RPIO.PUD_UP)

while True:
    if RPIO.input(button_pin) == False:
	print "button pressed"
