#!/usr/bin/python

#import the library to control the GPIO pins
import RPIO

#import the time library
import time

#gpio pin 14 is pin 8 on the raspberry pi (see the pin mapping on the workshop resources)
led_pin = 14

#setup the pin, and make it be off to start with
RPIO.setup(led_pin, RPIO.OUT, initial=RPIO.LOW)

#in a loop:
while True:
    print True
    #turn on the led
    RPIO.output(led_pin, True)
    #wait for 0.5 seconds
    time.sleep(0.5)
    print False
    #turn off the led
    RPIO.output(led_pin, False)
    #sleep again
    time.sleep(0.5)


