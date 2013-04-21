"""
author: matt venn
"""

#import the library
import RPIO

#gpio pin 4 is pin 7 on the p1 header
button_pin = 4

GPIO.setup(button_pin,GPIO.IN)

while True:
    if (GPIO.input(button_pin)):
        print("Button Pressed")
