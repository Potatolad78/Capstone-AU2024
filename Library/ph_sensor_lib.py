from machine import Pin, I2C, UART
from time import sleep
from picozero import RGBLED
import tsl2561
import random
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
        i2c= I2C(busNum, scl = Pin(sclPin), sda = Pin(sdaPin))
        self.sensor = tsl2561.TSL2561(i2c)
    def returnSensor(self):
        return self.sensor

class gps:
    def __init__(self):
        self.uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
        self.data_collected = False


class gps:
    def __init__(self, tx1, rx1):
        #TX should be 0 RX Should be 1
        self.uart = UART(0, baudrate=9600, tx=Pin(tx1), rx=Pin(rx1))
        self.data_collected = False
        self.time_utc = None
        self.latitude = None
        self.longitude = None
        self.lat_dir = None
        self.lon_dir = None

    def read(self):
        """Read and process GPS data, returning [time, latitude, longitude] once a valid $GPRMC sentence is parsed."""
        buffer = ""
        while True:  # Keep reading until valid data is found
            if self.uart.any():  # Check if there's data in the UART buffer
                buffer += self.uart.read().decode('utf-8')  # Read and decode data
                # Split the buffer into NMEA sentences
                sentences = buffer.split('\n')
                # Process all but the last sentence
                for sentence in sentences[:-1]:
                    if sentence.startswith('$GPRMC'):  # Process only $GPRMC sentences
                        if self._parse_nmea(sentence.strip()):  # Parse and check validity
                            # Return the GPS data as a list
                            return [self.time_utc, self.latitude, self.longitude]
                # Retain the last (possibly incomplete) sentence in the buffer
                buffer = sentences[-1]
            sleep(1)


    def _parse_nmea(self, nmea_sentence):
        """Parse a $GPRMC NMEA sentence for time, latitude, and longitude."""
        parts = nmea_sentence.split(',')
        if len(parts) >= 7:
            self.time_utc = self._parse_time(parts[1])
            self.latitude = self._convert_to_degrees(parts[3])
            self.lat_dir = parts[4]
            self.longitude = self._convert_to_degrees(parts[5])
            self.lon_dir = parts[6]

            if self.time_utc and self.latitude and self.longitude:
                self.data_collected = True
                print(f"Time (UTC): {self.time_utc}, Latitude: {self.latitude} {self.lat_dir}, Longitude: {self.longitude} {self.lon_dir}")

    @staticmethod
    def _convert_to_degrees(raw_value):
        """Convert NMEA raw data to degrees format."""
        if raw_value == '':
            return None
        try:
            raw_value = float(raw_value)
            degrees = int(raw_value // 100)
            minutes = raw_value - degrees * 100
            return degrees + minutes / 60  # Convert to decimal degrees
        except ValueError:
            return None

    @staticmethod
    def _parse_time(raw_time):
        """Convert NMEA raw time to HH:MM:SS format."""
        if raw_time == '':
            return None
        try:
            hours = int(raw_time[0:2])
            minutes = int(raw_time[2:4])
            seconds = int(raw_time[4:6])
            return f"{hours:02}:{minutes:02}:{seconds:02}"
        except (ValueError, IndexError):
            return None



class phSensor:

    def __init__(self, led, gps1, wPumpPin, dPumpPin, valvePin, lightSensor1):
        self.isMeassuring = True
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
            self.wPump = Pin(wPumpPin, Pin.OUT)
            self.dPump = Pin(dPumpPin, Pin.OUT)
            self.valve = Pin(valvePin, Pin.OUT)

        if not(isinstance(lightSensor1,lightSensor)):
            raise TypeError(f"Expected sixth input to be instance of lightSensor, but got {type(lightSensor1).__name__}.")

        else:
            self.lightSensor = lightSensor
        print(f"Sucessful creation of pH sensor class")

    def take_meassurments(self, color, sleepTime, loop):
        self.isMeassuring = True
        with open("results.csv", mode='w') as file:
            # Write the header row (if it's the first time writing the file, add a check)
            file.write("Test Number,Color,Time,Latitude,LongitudeAverage 1,Average 2,Average 3,Total Average\n")

            for i in range(loop):
                test_number = i + 1
                averages = []
                total_average = 0

                gps_data = self.gps.read()
                gps_time = gps_data[0]
                gps_lat = gps_data[1]
                gps_lon = gps_data[2]
                # Turn on the specified color LED
                if color.upper() == "RED":
                    self.led.turn_on_red(255)
                elif color.upper() == "GREEN":
                    self.led.turn_on_green(255)
                elif color.upper() == "BLUE":
                    self.led.turn_on_blue(255)
                elif color.upper() == "PURPLE":
                    self.led.turn_on_purple(255)
                else:
                    raise ValueError("Invalid color specified. Try Red, Blue, Green, or Purple")

                # Allow sensor to stabilize
                #self.lightSensor.read()
                sleep(sleepTime)

                # Take measurements
                for j in range(3):
                    average = 0
                    for k in range(5):
                        average += random.uniform(0.35, 0.8) #self.lightSensor.read()
                    average /= 5
                    averages.append(average)
                    total_average += average

                total_average /= 3

                # Turn off the LED
                self.led.turn_off_white()

                # Write the results to the file
                line = f"{test_number},{color.upper()},{gps_time},{gps_lat},{gps_lon},{averages[0]},{averages[1]},{averages[2]},{total_average}\n"
                file.write(line)
        self.isMeassuring = False
    

