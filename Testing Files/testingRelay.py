from machine import Pin
from time import sleep

turnOnPin = Pin(0, Pin.OUT)
pin2 = Pin(2,Pin.OUT)

turnOnPin.value(1)
pin2.value(1)
