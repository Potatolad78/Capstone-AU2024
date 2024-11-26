from machine import UART, Pin
import time

# Setup UART on the Raspberry Pi Pico
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

def read_gps():
    buffer = ""
    print(uart.any())
    while True:
        if uart.any():  # Check if there's any data in the buffer
            buffer += uart.read().decode('utf-8')  # Read and decode data
            # Split buffer into lines (NMEA sentences)
            sentences = buffer.split('\n')
            # Process all but the last (it may be incomplete)
            for sentence in sentences[:-1]:
                if sentence.startswith('$GPGGA') or sentence.startswith('$GPRMC'):
                    print(sentence)  # Print the full sentence for debug
                    parse_nmea(sentence.strip())
            # Keep the last sentence in case it is incomplete
            buffer = sentences[-1]  
        time.sleep(1)

def parse_nmea(nmea_sentence):
    # Example for GPGGA or GPRMC sentences, extract latitude and longitude
    parts = nmea_sentence.split(',')
    if nmea_sentence.startswith('$GPGGA'):
        if len(parts) >= 6:
            latitude = convert_to_degrees(parts[2])
            lat_dir = parts[3]
            longitude = convert_to_degrees(parts[4])
            lon_dir = parts[5]
            print(f"GPGGA - Latitude: {latitude} {lat_dir}, Longitude: {longitude} {lon_dir}")
        else:
            print(f"Invalid GPGGA sentence: {nmea_sentence}")

    
    elif nmea_sentence.startswith('$GPRMC'):
        if len(parts) >= 7:  
            latitude = convert_to_degrees(parts[3])
            lat_dir = parts[4]
            longitude = convert_to_degrees(parts[5])
            lon_dir = parts[6]
            print(f"GPRMC - Latitude: {latitude} {lat_dir}, Longitude: {longitude} {lon_dir}")
        else:
            print(f"Invalid GPRMC sentence: {nmea_sentence}")

def convert_to_degrees(raw_value):
    """ Convert NMEA raw data to degrees format """
    if raw_value == '':
        return None
    # NMEA format is dddmm.mmmm (degrees and minutes)
    try:
        raw_value = float(raw_value)
        degrees = int(raw_value // 100)
        minutes = raw_value - degrees * 100
        # Convert to decimal degrees
        return degrees + minutes / 60
    except ValueError:
        print(f"Invalid number format: '{raw_value}'")
        return None

# Start reading from the GPS
read_gps()
