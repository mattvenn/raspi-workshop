import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
led_pin = 8
GPIO.setup(led_pin, GPIO.OUT)

p = GPIO.PWM(led_pin, 50)
p.start(1)

while True:
    for dc in range(0,100):
        time.sleep(0.01)
        p.ChangeDutyCycle(dc)

