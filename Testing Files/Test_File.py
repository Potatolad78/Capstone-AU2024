from machine import Pin
from time import sleep

relay = Pin(9, Pin.OUT)
relay.value()

relay.value(1)
sleep(3)
relay.value(0)
