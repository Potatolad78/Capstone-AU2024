from machine import Pin, I2C
import tsl2561
from time import sleep

# set a manual ground pin for the light sensor
gnd = Pin(8, Pin.OUT)
gnd.value(0)

# light sensor I2C pins should be connected to desinated I2C Pico pins
# I2C bus 1 is GPIOs 6 (SDA) & 7 (SCL)
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
sensor = tsl2561.TSL2561(i2c)

while True:
    print(sensor.read()) # prints light intensity in lux Look for lux to nm coversion
    print(sensor.read(raw=True)) # prints raw digital counts for IR and broadband wavelengths
    sleep(0.5)
