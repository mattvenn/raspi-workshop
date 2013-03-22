#!/usr/bin/python
import RPIO
import time

#pin 8
led_pin = 14
RPIO.setup(led_pin, RPIO.OUT, initial=RPIO.LOW)

while True:
    print True
    RPIO.output(led_pin, True)
    time.sleep(0.5)
    print False
    RPIO.output(led_pin, False)
    time.sleep(0.5)


