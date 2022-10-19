import seeed_python_reterminal.core as rt
import seeed_python_reterminal.button as rt_btn
import RPi.GPIO as GPIO
import time
import asyncio

#Aquí se configura el pin GPIO numero 27, y el 29 
# como output para poder mandar señal a la impresora

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
print("Se ha configurado el pin GPIO 27 y 29 como OUT")


#prueba
print("pin 27  = 1")
GPIO.output(27, GPIO.HIGH)
time.sleep(0.5)
print("pin 27 = 0")
GPIO.output(27, GPIO.LOW)

#Se define la funcion que se usa para manar señal hacía la impresora
def estado_boton (bot, val):
	bot=str(bot)
	if bot == ButtonName.F1 & val == 1:
		GPIO.output(27, GPIO.HIGH)
		print("xF1,1")

	elif bot == ButtonName.F1 & val == 0:
		GPIO.output(27, GPIO.LOW)
		print("xF1, 0")

	elif bot == ButtonName.F2 & val == 1:
		GPIO.output(29, GPIO.HIGH)
		print("xF2, 1")

	elif bot == ButtonName.F2 & val == 0:
		GPIO.output(29, GPIO.LOW)
		print("xF2, 0")

# Funcion donde  se observa la actividad de los botones de la reTerminal para ver cuando se están presionando.
async def rutina_botones(device):
	async for event in device.async_read_loop():
		buttonEvent = rt_btn.ButtonEvent(event)
		if buttonEvent.name != None:
			print(f"bot={buttonEvent.name} val = {buttonEvent.value}")
			try:
				print(buttonEvent.name, buttonEvent.value)
			except:
				print("error")


boton_device = rt.get_button_device()
asyncio.ensure_future(rutina_botones(boton_device))
loop = asyncio.get_event_loop()
loop.run_forever()
