#!/usr/bin/python
import RPIO

#see http://elinux.org/RPi_Low-level_peripherals#GPIO_hardware_hacking
#gpio pin 4 is pin 7 on the p1 header
pir_pin = 4

def int(gpio_id, value):
    print "something happened!"

RPIO.add_interrupt_callback(pir_pin, int, edge='rising')
RPIO.wait_for_interrupts()

