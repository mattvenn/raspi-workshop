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
    print "got button #%d" % button
    if button == 1:
        print "raspberry pi!"
