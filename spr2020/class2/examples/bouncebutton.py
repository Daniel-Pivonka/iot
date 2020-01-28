import RPi.GPIO as GPIO
import time

def callback_one(pin):
    print("button press")

GPIO.setmode(GPIO.BCM)

GPIO.add_event_detect(21, GPIO.FALLING, callback_one, 1)

while True:
	pass

