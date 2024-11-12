import urtc
import tsl2561
from machine import Pin,I2C
from time import sleep
from servo import Servo
from machine import Pin, ADC
from time import sleep

# Servo on
servoPin = Pin(27, Pin.OUT)
servo = Servo(servoPin)

servo.write(100)
sleep(5)
servo.write(-50)
print("servo done")

# Assigns relays and sets to off
relay1 = Pin(22,Pin.OUT)
relay2 = Pin(28,Pin.OUT)
relay1.value(0)
relay2.value(0)

# Turn on pump relay
relay1.value(1) # pump on
sleep(2)        # fills for 2 sec
relay1.value(0) # pump off
print("pump done")

# Light sensor
# turn on LED - GREEN
# assign LED pins
led_r=Pin(15, Pin.OUT)
led_g=Pin(13, Pin.OUT)
led_b=Pin(14, Pin.OUT)

led_r.value(0)
led_g.value(0)
led_b.value(0)

# turn on LED BLUE
led_b.value(1)
sleep(2)
# take a light sensor reading
#i2c = I2C(1,scl=Pin(7),sda=Pin(6))
#sensor = tsl2561.TSL2561(i2c)
#blue_reading = sensor.read()
#print("blue", blue_reading)

led_b.value(0)

#LED.value(0) # turn off green light
led_r.value(1)
sleep(2)

# take a light sensor reading
#red_reading = sensor.read()
#print("red", red_reading)

led_r.value(0)

# open valve and close valve
relay2.value(1) # valve open
sleep(2)        # drains for 2 sec
relay2.value(0) # valve closed
print("valve done")

# save data
datafile=open("pH_data.csv",'a')
datafile.write(str(blue_reading) + ',' + str(red_reading) + '\n')
datafile.close()

# not sure what this is for
powerPin = Pin(5, Pin.OUT)
#i2c = I2C(,scl=Pin(5),sda=Pin(4))
#rtc = urtc.DS3231(i2c)
powerPin.value(1)
#print(rtc.datetime())









