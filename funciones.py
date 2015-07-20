import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

def iniciar_entrada(pin):
	GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
	print "Iniciar entrada en PIN: " + str(pin)

def iniciar_salida(pin):
	GPIO.setup(pin , GPIO.OUT)
	print "Iniciar salida en PIN: " + str(pin)
	# GPIO como salida

def apagar(pin):
	# GPIO.output( pin , False )
	GPIO.output(pin, GPIO.LOW)
	print "Apagando PIN: " + str(pin)

def delay(second):
	time.sleep( second )

def encender(pin):
	# GPIO.output( pin , True )
	GPIO.output(pin , GPIO.HIGH)
	print "Encendiendo PIN: " + str(pin)

def limpiar():
	GPIO.cleanup()
	print "Limpiando ..."

def test1(channel):
	print "value: " + str( GPIO.input(channel) )
	if GPIO.input(channel) == 0:
		encender(17)
	else:
		apagar(17)

try:
	iniciar_entrada(23)
	iniciar_salida(17)
	GPIO.add_event_detect(23, GPIO.BOTH, callback=test1)
	delay(300)
finally:
	limpiar()