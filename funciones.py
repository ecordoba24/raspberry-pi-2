import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) ## GPIO 17 como salida
# GPIO.setup(27, GPIO.OUT) ## GPIO 27 como salida

def iniciar(pin):
	print "Iniciar PIN: " + str(pin)
	GPIO.setup( pin , GPIO.OUT )

def apagar(pin):
	print "Apagando PIN: " + str(pin)
	GPIO.output( pin , False )

def delay(second):
	time.sleep( second )

def encender(pin):
	print "Encendiendo PIN: " + str(pin)
	GPIO.output( pin , True )

def limpiar():
	print "Limpiando ..."
	GPIO.cleanup()

'''
def blink():
        print "Ejecucion iniciada..."
        iteracion = 0
        while iteracion < 30: ## Segundos que durara la funcion
                GPIO.output(17, True) ## Enciendo el 17
                GPIO.output(27, False) ## Apago el 27
                time.sleep(1) ## Esperamos 1 segundo
                GPIO.output(17, False) ## Apago el 17
                GPIO.output(27, True) ## Enciendo el 27
                time.sleep(1) ## Esperamos 1 segundo
                iteracion = iteracion + 2 ## Sumo 2 porque he hecho dos parpadeos
        print "Ejecucion finalizada"
        GPIO.cleanup() ## Hago una limpieza de los GPIO
'''

iniciar(17)
iniciar(27)

encender(27)
delay(2)
apagar(27)
encender(17)
delay(2)
apagar(17)

limpiar()

# blink() ## Hago la llamada a la funcion blink
