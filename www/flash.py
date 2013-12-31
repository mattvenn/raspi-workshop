#import the library to control the GPIO pins
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#import the time library
import time

led_pin = 8

#setup the pin, and make it be off to start with
GPIO.setup(led_pin, GPIO.OUT)

#turn on the led
print(True)
GPIO.output(led_pin, True)
#wait for 0.5 seconds
time.sleep(0.5)

#turn off the led
print(False)
GPIO.output(led_pin, False)
