#!/usr/bin/python
import RPIO
import time
#see http://elinux.org/RPi_Low-level_peripherals#GPIO_hardware_hacking

#gpio pin 4 is pin 7 on the p1 header
step_pin = 4
#gpio pin 17 is pin 9 on the p1 header
dir_pin = 17

RPIO.setup(step_pin, RPIO.OUT, initial=RPIO.LOW)
RPIO.setup(dir_pin, RPIO.OUT, initial=RPIO.LOW)

dir = False

while True:
	for i in range(100):
		RPIO.output(step_pin, True)
		time.sleep(0.01)
		RPIO.output(step_pin, False)
		time.sleep(0.01)
	RPIO.output(dir_pin, dir)
	dir = not dir
	
