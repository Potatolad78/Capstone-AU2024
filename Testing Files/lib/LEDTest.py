from machine import Pin
from time import sleep
from RGBLightLibrary import RGBLight
import urtc
from servo import Servo
from machine import Pin, I2C
purpleLed = RGBLight(0,1,2)
greenLed = RGBLight(19,20,21)
pin15 = Pin(15, Pin.OUT)
servo = Servo(pin15)
i2c = I2C(0, scl=Pin(17), sda = Pin(16))
print(i2c.scan())
pin9 =  Pin(9, Pin.OUT)
rtc = urtc.DS3231(i2c)


for x in range(180):
    print(rtc.datetime())
    greenLed.turnOnGreen(255)
    purpleLed.turnOnPurple()
    pin9.value(1)
    servo.write(x)
    sleep(0.1)
    greenLed.turnOffGreen()
    purpleLed.turnOffPurple()
    pin9.value(0)
    sleep(0.1)



def runPump():
    return;

#Half a second for pump to be on
# turn on then off then back on then half a second on then off
# On half a second off half a second on half second then off till turned back on
#rgb1.color = (255, 0 ,10 )
#print(rgb1.color[0])
