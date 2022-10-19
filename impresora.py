import seeed_python_reterminal.core as rt
import time
import seeed_python_reterminal.button as rt_btn

device = rt.get_button_device()

while True:
	for event in device.read_loop():
		buttonEvent = rt_btn.ButtonEvent(event)
		if buttonEvent.name != None:
			print("name={str(buttonEvent.name)} value = {buttonEvent.value}")
