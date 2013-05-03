#import the library to control the GPIO pins
import RPIO
RPIO.setwarnings(False)

#import the time library
import time

#gpio pin 14 is pin 8 on pi
led_pin = 14

#setup the pin, and make it be off to start with
RPIO.setup(led_pin, RPIO.OUT, initial=RPIO.LOW)

#flash the led just once

#turn on the led
RPIO.output(led_pin, True)
#wait for 0.5 seconds
time.sleep(0.5)
#turn off the led
RPIO.output(led_pin, False)
#sleep again
time.sleep(0.5)


