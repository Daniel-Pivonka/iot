import RPi.GPIO as GPIO

#setup board
GPIO.setmode(GPIO.BCM)

#setup pin as input
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)


clickedflag = False

#loop endlessly
while True:

		#get button state
        switchstate = GPIO.input(21)


		if (buttonstate and not clickedflag)
			clickedflag = True;


  
  		if (not buttonstate and clickedflag)
    		clickedflag = False;
			print ('clicked')
