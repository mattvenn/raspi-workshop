#!/usr/bin/python
"""
author: matt venn, based on Adafruit's example
"""

from Adafruit_BMP085 import BMP085

#initialise the sensor
bmp = BMP085(0x77)

def read_sensor():
	temp = bmp.readTemperature()
	pressure = bmp.readPressure()
	altitude = bmp.readAltitude()
	return( temp,pressure,altitude )

#if this script is run from the command line...
if __name__=="__main__":  
	(temp,pressure,altitude)=read_sensor()
	print "Temperature: %.2f C" % temp
	print "Pressure:    %.2f hPa" % (pressure / 100.0)
	print "Altitude:    %.2f" % altitude
