import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

p = GPIO.PWM(8, 50)
p.start(1)

while True:
    for dc in range(0,100):
        time.sleep(0.01)
        p.ChangeDutyCycle(dc)

