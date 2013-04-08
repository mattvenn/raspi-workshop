#!/usr/bin/python
"""
author: matt venn
"""

import serial

serial_port=serial.Serial()
serial_port.port='/dev/ttyACM0'
serial_port.baudrate=9600
serial_port.open()

while True:
    response = serial_port.readline()
    button = int(response.strip())

    #depending on what button is pressed, do different things
    if button == 0:
        print "green"
    elif button == 1:
        print "pink"
    elif button == 2:
        print "blue"
    elif button == 3:
        print "yellow"
    else:
        print "don't know that button"
