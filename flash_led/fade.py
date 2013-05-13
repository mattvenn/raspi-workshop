#import the library to control the GPIO pins
from RPIO import PWM
PWM.setup()

#get rid of debug output
PWM.set_loglevel(PWM.LOG_LEVEL_ERRORS)

import time

#we have a certain number of pwm channels we can use
dma = 0
PWM.init_channel(dma)

led_pin = 14

PWM.add_channel_pulse(dma,led_pin,0,0)
while True:
    for width in range(0,1999,40):
        #width can go from 0 (off) to 1999 (full bright)
        PWM.add_channel_pulse(dma,led_pin,0,width)
        time.sleep(0.05)
        print width

