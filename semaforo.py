import RPi.GPIO as GPIO
import time
import datetime
GPIO.setmode(GPIO.BCM)

print datetime.datetime.now()

def iniciar_entrada(pin):
	GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
	print "Iniciar entrada en PIN: " + str(pin)

def iniciar_salida(pin):
	GPIO.setup(pin , GPIO.OUT)
	print "Iniciar salida en PIN: " + str(pin)
	# GPIO como salida

def apagar(pin):
	# GPIO.output( pin , False )
	GPIO.output(pin, True)
	# GPIO.output(pin, GPIO.LOW)
	print "Apagando PIN: " + str(pin)

def delay(second):
	time.sleep( second )

def encender(pin):
	# GPIO.output( pin , True )
	GPIO.output(pin, False)
	# GPIO.output(pin , GPIO.HIGH)
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

def test2():
	i = 0
	while i < 10:
		encender(17)
		delay(0.5)
		apagar(17)
		delay(0.5)	
		i += 1

def parpadear(pin, cantidad, tiempo):
	print("pin: "+str(pin)+" cantidad: "+str(cantidad)+" tiempo: "+str(tiempo) )
	i = 1
	while i <= int(cantidad):
		encender(pin)
		delay(tiempo)
		apagar(pin)
		delay(tiempo)
		i=i+1
		

def semaforo():
	encender(6)
	delay(2)
	parpadear(6, 3, 0.2)
	encender(22)
	delay(1)
	parpadear(22, 3, 0.2)
	encender(17)
	delay(3)
	parpadear(17, 3, 0.3)
	
	# encender(17)
	# encender(22)
	# encender(6)


try:
	iniciar_entrada(23)
	iniciar_salida(17)  # rojo
	iniciar_salida(22)  # amarillo
	iniciar_salida(6)    # verde
	GPIO.add_event_detect(23, GPIO.BOTH, callback=test1)
	while True:
		semaforo()
	delay(2)
	print ("FIN!!!")
finally:
	limpiar()
