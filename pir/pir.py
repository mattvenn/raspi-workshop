"""
author: matt venn
"""

#the library for the pin control
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

pir_pin = 8

#set the pin to be high to start, low when pressed
GPIO.setup(pir_pin,GPIO.IN, pull_up_down=GPIO.PUD_UP)

print "waiting..."
while True:
    if GPIO.input(pir_pin) == True:
        print "pir detected"
        while GPIO.input(pir_pin) == True:
            #wait for the pin to go low
            pass
        print "waiting..."
