"""
author: matt venn
"""

#import the library
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

button_pin = 16

#set the pin to be high to start, low when pressed
GPIO.setup(button_pin,GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(button_pin) == False:
        print "button pressed"


