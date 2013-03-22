#!/usr/bin/python

import serial

serial_port=serial.Serial()
serial_port.port='/dev/ttyACM0'
serial_port.baudrate=9600
serial_port.open()

while True:
	response = serial_port.readline()
	button = int(response.strip())
	for num in range(4):
		if button == num:
			print "got button #%d" % num
