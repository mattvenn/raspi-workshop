#!/usr/bin/python
"""
author: matt venn
"""

#the library for the pin control
import RPIO

#gpio pin 4 is pin 7 on the p1 header
pir_pin = 4

#the interrupt function
def int(gpio_id, value):
    print "something happened!"

#setup the interrupt so it get's called with the output from the sensor goes high
RPIO.add_interrupt_callback(pir_pin, int, edge='rising')
RPIO.wait_for_interrupts()
