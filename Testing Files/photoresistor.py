from machine import Pin, ADC
from time import sleep
#photo_pin = ADC(26)
#while True:
#    val = photo_pin.read_u16()
#    print(val)
#    time.sleep(0.2)
led_r=Pin(1, Pin.OUT)
led_g=Pin(2, Pin.OUT)
led_b=Pin(3, Pin.OUT)

led_r.value(1)
led_g.value(1)
led_b.value(1)

while True:
    led_r.value(0)
    sleep(0.2)
    led_r.value(1)
    
    led_g.value(0)
    sleep(0.2)
    led_g.value(1)
    
    led_b.value(0)
    sleep(0.2)
    led_b.value(1)
    sleep(0.2)
    