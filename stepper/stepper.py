#!/usr/bin/python
"""
author: matt venn"
"""

#import the RPIO library
import RPIO
import time
RPIO.setwarnings(False)

#gpio pin 4 is pin 7 on the p1 header
step_pin = 4
#gpio pin 17 is pin 11 on the p1 header
dir_pin = 17
#setup the pins
RPIO.setup(step_pin, RPIO.OUT, initial=RPIO.LOW)
RPIO.setup(dir_pin, RPIO.OUT, initial=RPIO.LOW)

#a variable to know if we should go forwards or backwards
dir = False

#then in a loop, step the motor forwards and backwards
sleep_time=0.01
while True:
    print dir
    #move 50 steps
    for i in range(200):
        RPIO.output(step_pin, True)
        time.sleep(sleep_time)
        RPIO.output(step_pin, False)
        time.sleep(sleep_time)

    #change direction
    RPIO.output(dir_pin, dir)
    dir = not dir
