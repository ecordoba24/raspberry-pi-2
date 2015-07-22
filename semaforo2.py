# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
try:
	GPIO.output(17, 0)
	time.sleep(2)
	# print ("FIN!!!")
finally:
	GPIO.cleanup()
