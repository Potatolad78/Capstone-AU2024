# This script prints temperature readings from a DS18B20 sensor

from machine import Pin
import urtc
from machine import Pin, I2C
i2c = I2C(0, scl=Pin(17), sda = Pin(16))
print(i2c.scan())
rtc = urtc.DS3231(i2c)
print(rtc.datetime())
