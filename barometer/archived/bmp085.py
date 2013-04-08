#!/usr/bin/python
import subprocess
import re

#run the c program
p = subprocess.Popen( [ "sudo", "./testBMP085" ] , stdout=subprocess.PIPE )
stdout,stderr = p.communicate()

#find the temp and store to variable
m = re.search("Temperature\s+(\d+\.\d*)",stdout)
temp = m.group(1)

#find the pressure and store to variable
m = re.search("Pressure\s+(\d+\.\d*)",stdout)
pressure = m.group(1)

print temp, pressure

