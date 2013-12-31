"""
author: matt venn
"""

#import the PWM part of the GPIO library
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#import the time library
import time

servo_pin = 8
GPIO.setup(servo_pin, GPIO.OUT)
freq = 1/0.02
p = GPIO.PWM(servo_pin, freq)
p.start(3)

#forever...
while True:
    #change the angle by changing the PWM pulse width, this works between 1 and 10
    print(True)
    p.ChangeDutyCycle(3)
    #sleep
    time.sleep(0.5)
    print(False)
    # change the angle
    p.ChangeDutyCycle(5)
    #sleep
    time.sleep(0.5)
