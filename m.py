from gpiozero import LED
from time import sleep

led = LED(17)

led.On()
sleep(0.75)
led.Off()
sleep(0.25)
led.On()
sleep(0.75)
led.Off()
sleep(0.75)
