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

def step(dir,step_time=0.01):
    #set the direction
    RPIO.output(dir_pin, dir)

    #take a step
    RPIO.output(step_pin, True)
    time.sleep(step_time)
    RPIO.output(step_pin, False)
    time.sleep(step_time)


#if this script is run from the command line...
if __name__=="__main__":  
    while True:
        for i in range(200):
            step(dir)

        #change direction
        dir = not dir
        print dir

