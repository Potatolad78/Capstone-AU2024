from machine import Pin
from time import sleep

turnOnPin = Pin(10, Pin.OUT)

turnOnPin.value(1)
sleep(5)
turnOnPin.value(0)