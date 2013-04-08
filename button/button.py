#!/usr/bin/python
"""
author: matt venn
"""

#import the library
import RPIO

#gpio pin 4 is pin 7 on the p1 header
button_pin = 4

#define a function that will get called when we get an interrupt
def int(gpio_id, value):
    print "something happened!"

#enable pin's pullup. set the interrupt on falling edge
RPIO.add_interrupt_callback(button_pin, int, pull_up_down=RPIO.PUD_UP, edge='falling')

#wait for things to happen
RPIO.wait_for_interrupts()
