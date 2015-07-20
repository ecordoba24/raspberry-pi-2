import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

try:
	GPIO.setup(17 , GPIO.OUT)
	GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	while True:
	    input_state = GPIO.input(23)
	    print input_state
	    if input_state == 1:
	       GPIO.output(17, GPIO.LOW)
	    else:
	      GPIO.output(17, GPIO.HIGH)
finally:
	GPIO.cleanup()

