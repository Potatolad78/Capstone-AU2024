import serial
import time

def send_command_to_pico(command):
    pico_serial = serial.Serial('COM4', 115200, timeout=0.1)  # Longer timeout
    time.sleep(2)  # Allow Pico to initialize

    # Send command
    pico_serial.write(command.encode() + b'\n')
    print(f"Sent command: {command}")

    responses = []
    while True:
        response = pico_serial.readline().decode().strip()
        if response:
            responses.append(response)
            print(f"Received response: {response}")
            if "Measurement complete." in response:
                break

    pico_serial.close()
    return responses

# Close the serial connection
def receive_file_from_pico(command, output_file):
    """
    Sends a command to the Pico to send a file, then saves the received data to a file.
    """
    pico_serial = serial.Serial('COM4', 115200, timeout=1)  # Adjust as needed
    time.sleep(2)  # Allow Pico to initialize

    # Send the command to the Pico
    pico_serial.write(command.encode() + b'\n')
    print(f"Sent command: {command}")

    with open(output_file, "a") as f:
        while True:
            response = pico_serial.readline().decode().strip()
            if response == "EOF":
                print("File transfer complete.")
                break
            elif response:  # Write each line to the file
                f.write(response + "\n")
                print(f"Received: {response}")

    pico_serial.close()
# Example usage: Send a 'collect_data' command
send_command_to_pico("collect_data")

# Example usage: Send a 'send_file' command to retrieve the file
receive_file_from_pico("send_file", "data.csv")