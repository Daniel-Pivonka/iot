import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
        switchstate = GPIO.input(21)
        print (switchstate)

