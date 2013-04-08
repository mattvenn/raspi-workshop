#!/usr/bin/python
"""
author: matt venn
"""

#import the PWM part of the RPIO library
from RPIO import PWM
#import the time library
import time

#create the servo object
servo = PWM.Servo()

#gpio pin 14 is pin 8 on the pi
servo_pin = 14

#forever...
while True:
  #change the angle by changing the PWM pulse width
	servo.set_servo(servo_pin, 4000)
  #sleep
	time.sleep(0.5)
  # change the angle
	servo.set_servo(servo_pin, 2000)
  #sleep
	time.sleep(0.5)
