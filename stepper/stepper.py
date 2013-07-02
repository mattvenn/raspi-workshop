"""
author: matt venn"
"""

#import the RPIO library
import RPIO
import time
RPIO.setwarnings(False)
RPIO.setmode(RPIO.BOARD)

step_pin = 7
dir_pin = 11
#setup the pins
RPIO.setup(step_pin, RPIO.OUT, initial=RPIO.LOW)
RPIO.setup(dir_pin, RPIO.OUT, initial=RPIO.LOW)

#a variable to know if we should go forwards or backwards
dir = False

def step(dir=False,step_time=0.01):
    #set the direction
    RPIO.output(dir_pin, dir)

    #take a step
    RPIO.output(step_pin, True)
    time.sleep(step_time)
    RPIO.output(step_pin, False)
    time.sleep(step_time)


while True:
    for i in range(200):
        step(dir)

    #change direction
    dir = not dir
    print dir

