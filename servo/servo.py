#!/usr/bin/python
# Setup PWM.Servo with the default 20ms subcycle
from RPIO import PWM
import time

servo = PWM.Servo()

#gpio pin 14 is pin 8

while True:
	# Set a 4000us (4ms) pulse every 20ms for GPIO 14:
	servo.set_servo(14, 4000)
	time.sleep(0.5)
	servo.set_servo(14, 2000)
	time.sleep(0.5)
