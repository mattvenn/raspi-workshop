import scratch
#see https://github.com/pilliq/scratchpy for details on scratch module
import sys

#import the time library
import time

#import the library to control the GPIO pins
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


led_pin = 8

#setup the pin, and make it be off to start with
GPIO.setup(led_pin, GPIO.OUT)


ip = '127.0.1.1'
port = 42001
if len(sys.argv) == 2:
    ip = sys.argv[1]

print "trying to connect to", ip, ":", port
try:
    s = scratch.Scratch(host=ip, port=port) 
except scratch.ScratchError, e:
    print "couldn't connect - is scratch running?"
    print e
    exit(1)
print "connected"

def listen():
    while True:
        try:
           yield s.receive()
        except scratch.ScratchError:
           raise StopIteration

for msg in listen():
    # code to handle broadcasts
    if msg[0] == 'broadcast':
        if msg[1] == 'on':
            print "got on"
            GPIO.output(led_pin, True)
        elif msg[1] == 'off':
            print "got off"
            GPIO.output(led_pin, False)
        else:
            print "didn't recognise broadcast: ", msg
