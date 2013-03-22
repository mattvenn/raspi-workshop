#!/usr/bin/python
import RPIO

#see http://elinux.org/RPi_Low-level_peripherals#GPIO_hardware_hacking
#gpio pin 4 is pin 7 on the p1 header
button_pin = 4

def int(gpio_id, value):
    print "something happened!"

#enable pin's pullup. Interrupt on falling edge
RPIO.add_interrupt_callback(button_pin, int, pull_up_down=RPIO.PUD_UP, edge='falling')
RPIO.wait_for_interrupts()

