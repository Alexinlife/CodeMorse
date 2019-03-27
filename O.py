from gpiozero import LED
from time import sleep

led = LED(17)

while True:
led.on
sleep(0.75)
led.off
sleep(0.25)
led.on
sleep(0.75)
led.off
sleep(0.25)
led.on
sleep(0.75)
led.off
sleep(0.75)
