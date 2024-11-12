# import necessary libraries and functions
#import tsl2591
from machine import Pin, I2C
from tsl2591 import TSL2591, INTEGRATIONTIME_100MS, GAIN_LOW
import time

# assign pins for the clock and the light sensor
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
print(i2c.scan())
time.sleep(2)
#sensor = TSL2591(integration=INTEGRATIONTIME_100MS, gain=GAIN_LOW)
sensor = TSL2591(i2c)
lux = sensor.sample()
print(lux)

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
I2C_ADDR = i2c.scan()[0]
print(hex(I2C_ADDR))