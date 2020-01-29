import RPi.GPIO as GPIO
import time


#function will be call for event
def callback_one(pin):
    print("button press")

#setup board
GPIO.setmode(GPIO.BCM)

#setup pin to detect event 
GPIO.add_event_detect(21, GPIO.FALLING, callback_one, 1)

#loop endlessly
while True:
	pass

