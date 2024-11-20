from machine import Pin, I2C
import csv
from time import sleep
from picozero import RGBLED
import tsl2561
class RGBLight():
    def __init__(self, r, g, b):
        self.RGB = RGBLED(red = r, green = g, blue = b)

    def turn_on_green(self, intensity):
        self.RGB.color = (self.RGB.color[0], intensity, self.RGB.color[2])
    
    def turn_on_red(self, intensity):
        self.RGB.color = (intensity,self.RGB.color[1] ,self.RGB.color[2])
    
    def turn_on_blue(self, intensity):
        self.RGB.color = (self.RGB.color[1],self.RGB.color[1],intensity)

    def turn_on_purple(self, intensity):
        self.turn_on_red(intensity)
        self.turn_on_blue(intensity)

    def turn_on_white(self):
        self.turn_on_blue()
        self.turn_on_green()
        self.turn_on_red()

    def turn_on_RGB(self, r, g, b):
        self.RGB.color = (r,g,b)

    def turn_off_green(self):
        self.RGB.color = (self.RGB.color[0],0,self.RGB.color[2])
    
    #Turns off the red led
    def turn_off_red(self):
        self.RGB.color = (0,self.RGB.color[1],self.RGB.color[2])
    
    #Turns off the blue led
    def turn_off_blue(self):
        self.RGB.color = (self.RGB.color[0],self.RGB.color[1],0)
        
    def turn_off_purple(self):
        self.turnOffRed()
        self.turnOffBlue()
    
    def turn_off_white(self):
        self.turn_off_blue()
        self.turn_off_green()
        self.turn_off_red()
    
    def cycle_through_light(self):
        self.turn_off_white()

        self.turn_on_red(255)
        sleep(5)
        self.turn_off_red()

        self.turn_on_green(255)
        sleep(5)
        self.turn_off_green()

        self.turn_on_blue(255)
        sleep(5)
        self.turn_off_blue()

class lightSensor:
    def __init__(self,busNum,sclPin,sdaPin):
        pass
    #    i2c= I2C(busNum, scl = Pin(sclPin), sda = Pin(sdaPin))
    #    self.sensor = tsl2561.TSL2561(i2c)
    #def returnSensor(self):
    #    return self.sensor

class gps:
    def __init__(self):
        pass

class phSensor:

    def __init__(self, led, gps1, wPumpPin, dPumpPin, valvePin, lightSensor1):
        if not(isinstance(led,RGBLight)):
            raise TypeError(f"Expected first input to be instance of RGBLight, but got {type(led).__name__}.")
        else:
            self.led = led
        if not(isinstance(gps1, gps)):
            raise TypeError(f"Expected second input to be instance of gps, but got {type(gps1).__name__}.")
        else:
            self.gps = gps1
        if not(isinstance(wPumpPin, int) or isinstance(dPumpPin, int) or isinstance(valvePin, int)):
            raise TypeError(f"Expected third through fifth inputs to be integers but got{type(wPumpPin).__name__},{type(dPumpPin).__name__},{type(valvePin).__name__}.")
        
        else:
            self.wPump = Pin(wPumpPin. Pin.OUT)
            self.dPump = Pin(dPumpPin, Pin.OUT)
            self.valve = Pin(valvePin, Pin.OUT)

        if not(isinstance(lightSensor1,lightSensor)):
            raise TypeError(f"Expected sixth input to be instance of lightSensor, but got {type(lightSensor1).__name__}.")

        else:
            self.lightSensor = lightSensor
        print(f"Sucessful creation of pH sensor class")

    def take_meassurments(self, color, sleepTime, sensor, loop):
        with open("results.csv", mode='a', newline="") as file:
            writer = csv.writer

            writer.writerow(["Test Number", "Color", "Average 1 ", "Average 2", "Average 3", "Total Average"])
            for i in range(loop):
                test_number = i + 1
                averages = []
                total_average =  0

                if (color.upper() == "RED"):
                    self.led.turn_on_red(255)
                elif(color.upper() == "GREEN"):
                    self.led.turn_on_green(255)
                elif(color.upper() == "BLUE"):
                    self.led.turn_on_blue(255)
                elif(color.upper() == "PURPLE"):
                    self.led.turn_on_purple(255)
                else:
                    raise ValueError("Invalid color specified. Try Red, Blue, Green, or Purple")
                
                sensor.read()
                sleep(sleepTime)
                for j in range(3):
                    average = 0
                    for k in range(5):
                        average += sensor.read()
                    average /= 5
                    averages.append(average)
                    total_average += average
                total_average /= 3

                self.led.turn_off_white()

                writer.writerow([test_number, color.upper(), averages[0], averages[1], averages[2], total_average])

                  

