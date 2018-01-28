from gpiozero import LED
from time import sleep

red = LED(16)
yellow = LED(20)
green = LED(21)

while True:
    red.on()
    sleep(5)
    yellow.on()
    sleep(2)
    red.off()
    yellow.off()

    green.on()
    sleep(4)
    green.off()
    sleep(0.5)
    green.on()
    sleep(0.5)
    green.off()
    sleep(0.5)
    green.on()
    sleep(0.5)
    green.off()
    sleep(0.5)
    green.on()
    sleep(0.5)
    green.off()
    yellow.on()
    sleep(1)
    yellow.off()

