#!/usr/bin/python
import RPIO
from RPIO import PWM
import time
#see http://elinux.org/RPi_Low-level_peripherals#GPIO_hardware_hacking

#gpio pin 4 is pin 7 on the p1 header
step_pin = 4
#gpio pin 17 is pin 11 on the p1 header
dir_pin = 17
#gpio pin 14 is pin 8
pwm_pin = 14

#setup the pins
RPIO.setup(step_pin, RPIO.OUT, initial=RPIO.LOW)
RPIO.setup(dir_pin, RPIO.OUT, initial=RPIO.LOW)

#use pwm to control current to stepper motor
PWM.setup()
dma_channel=0
PWM.init_channel(dma_channel,20000)

#this pwm setting causes the demo motor to draw 250mA
PWM.add_channel_pulse(dma_channel, pwm_pin, 0, 1500)

#then in a loop, step the motor forwards and backwards
dir = False
while True:
	print dir
	for i in range(50):
		RPIO.output(step_pin, True)
		time.sleep(0.01)
		RPIO.output(step_pin, False)
		time.sleep(0.01)
	RPIO.output(dir_pin, dir)
	dir = not dir
	
