import RPi.GPIO as GPIO

#setup board
GPIO.setmode(GPIO.BCM)

#setup pin as input
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#var
clickedflag = False

#loop endlessly
while True:

		#get button state
		buttonstate = GPIO.input(21)

		#if the button is pressed and was not previously clicked
		if (buttonstate and not clickedflag):
			#set as clicked
			clickedflag = True;

		#if button is not clicked and was previously not clicked 
		if (not buttonstate and clickedflag):
			#set as not clicked
			clickedflag = False;

			#print
			print ('clicked')
