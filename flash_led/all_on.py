#import the library to control the GPIO pins
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#a list of all the pins
pins = [ 3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 23, 24, 26 ]

#turn on all pins
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, True)

