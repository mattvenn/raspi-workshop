"""
author: matt venn"
"""

#import the GPIO library
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

step_pin = 7
dir_pin = 11
#setup the pins
GPIO.setup(step_pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(dir_pin, GPIO.OUT, initial=GPIO.LOW)

#a variable to know if we should go forwards or backwards
dir = False

def step(dir,step_time):
    #set the direction
    GPIO.output(dir_pin, dir)

    #take a step
    GPIO.output(step_pin, True)
    time.sleep(step_time)
    GPIO.output(step_pin, False)
    time.sleep(step_time)


while True:
    for i in range(200):
        step(dir,0.01)

    #change direction
    dir = not dir
    print(dir)

