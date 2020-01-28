import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)


GPIO.output(18,GPIO.HIGH)
print(GPIO.input(18))
time.sleep(1)
GPIO.output(18,GPIO.LOW)
print(GPIO.input(18))
