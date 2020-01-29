import RPi.GPIO as GPIO
import time

#setup board
GPIO.setmode(GPIO.BCM)

#setup pins
GPIO.setup(18, GPIO.OUT)

#turn pin on
GPIO.output(18,GPIO.HIGH)

#print state of pin
print(GPIO.input(18))

#wait one second
time.sleep(1)

#turn pin off
GPIO.output(18,GPIO.LOW)

#print state of pin
print(GPIO.input(18))
