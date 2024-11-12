from RGBLightLibrary import RGBLight, servoMove, powerRelay, lightSensor
from machine import Pin
from time import sleep


light = lightSensor(1,3,2)
lightSensor = light.returnSensor()

print(lightSensor.read())


#3.25 Warm up to 0.1 per spit
relay1 = Pin(18, Pin.OUT)
relay2 = Pin(19, Pin.OUT)
relay3 = Pin(20, Pin.OUT)
relay1.value(1)
sleep(20)
relay1.value(0)
sleep(0.3)
relay1.value(1)
relay2.value(1)
sleep(0.1)
relay1.value(0)
sleep(2.4)
relay2.value(0)
sleep(5)
relay3.value(1)
sleep(10)
relay3.value(0)
relay1.value(1)
sleep(10)
relay1.value(0)