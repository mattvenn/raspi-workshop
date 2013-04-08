#!/usr/bin/python
# Setup PWM.Servo with the default 20ms subcycle
from RPIO import PWM
import time

servo = PWM.Servo()

#gpio pin 14 is pin 8
servo_pin = 14

#start and stop angles
start_pwm = 2000
end_pwm = 4000

while True:
	print "CW"
	# Set a 4000us (4ms) pulse every 20ms for GPIO 14:
	servo.set_servo(servo_pin, start_pwm)
	time.sleep(0.5)

	print "CCW"
	servo.set_servo(servo_pin, end_pwm)
	time.sleep(0.5)
