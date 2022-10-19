import seeed_python_reterminal.core as rt
import time
import seeed_python_reterminal.button as rt_btn
import  RPi.GPIO as GPIO

#Aquí se configura el pin GPIO numero 27
# como output para poder mandar señal a la impresora

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27, GPIO.OUT)

#prueba
print("pin 27  = 1")
GPIO.output(27, GPIO.HIGH)
time.sleep(1)
print("pin 27 = 0")
GPIO.output(27, GPIO.LOW)

# Aquí se observa la actividad de los botones de la reTerminal para ver cuando se están presionando.
device = rt.get_button_device()
while True:
	for event in device.read_loop():
		buttonEvent = rt_btn.ButtonEvent(event)
		if buttonEvent.name != None:
			print(f"name={str(buttonEvent.name)} value = {buttonEvent.value}")
			print(buttonEvent.name, buttonEvent.value)
