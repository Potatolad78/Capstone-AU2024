import sys
import utime
import os
import time
from time import sleep
from machine import Pin
from ph_sensor_lib import *
blue = Pin(15, Pin.OUT)
blue.value(1)
sleep(1.5)
blue.value(0)
ps = phSensor(RGBLight(14,13,15),gps(0,1), 19, 18, 20, lightSensor(1,3,2))

# Main loop to listen for commands over USB
print("Waiting for commands over USB...")

buffer = ""  # This will store the incoming characters
out_file = "out.txt"  # Define the output file name

while True:
        
    char = sys.stdin.read(1)  # Read one character at a time
    if char == "\n":  # End of command
        command = buffer.strip()  # Process the complete command
        buffer = ""  # Reset buffer
        
        print(f"Received command: {command}")
        
        # Process the command
        if command == "collect_data":
            print("Collecting data...")
            ps.take_meassurments("green", 5, 3)
            sys.stdout.write("Measurement complete.\n")
            # Add logic to handle data collection, e.g., turning on a pin
            # Example of GPIO operation (if using a Raspberry Pi)

        elif command == "send_file":
            try:
                with open("results.csv", "r") as f:
                    for line in f:
                        sys.stdout.write(line)  # Send each line
                    sys.stdout.write("EOF\n")  # Indicate end of file
            except FileNotFoundError:
                sys.stdout.write("File not found.\n")

        else:
            sys.stdout.write("unknown_command\n")

        # Write the command to the file
        with open(out_file, "a") as f:  # 'a' mode appends to the file
            f.write(f"Received command: {command}\n")

    else:
        buffer += char  # Add character to buffer

    time.sleep(0.1)  # Small delay to prevent high CPU usage
