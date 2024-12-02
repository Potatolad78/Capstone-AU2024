import serial
import time
import pandas as pd
import matplotlib.pyplot as plt 
import os

def clean_data(file_name):
    """
    Cleans the data file by skipping lines that contain the specific text 'Received command'.
    """
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Filter lines that don't contain the unwanted text
    cleaned_lines = [line for line in lines if 'Received command' not in line]

    # Write cleaned data to a temporary file
    cleaned_file_name = "cleaned_" + file_name
    with open(cleaned_file_name, 'w') as temp_file:
        temp_file.writelines(cleaned_lines)

    # Read the cleaned data into a DataFrame
    data = pd.read_csv(cleaned_file_name)
    return data

def interpolate_x(df, target_y):
    """
    Interpolates the x-value for a given target y-value based on the calibration curve data.
    """
    for i in range(len(df) - 1):
        y1, y2 = df.iloc[i]['y'], df.iloc[i + 1]['y']
        if (y1 <= target_y <= y2) or (y1 >= target_y >= y2):
            x1, x2 = df.iloc[i]['x'], df.iloc[i + 1]['x']
            target_x = x1 + (target_y - y1) * (x2 - x1) / (y2 - y1)
            return target_x
    return None  # Return None if target_y is out of range

def draw_graph(file_name):
    """
    Draws a graph based on the cleaned data and calibration curve and adds interpolated pH values to the file.
    """
    # Calibration curve data
    calibration_curve = pd.DataFrame({
        'x': [5, 7, 9],  # Known x-values (pH values)
        'y': [0.982363, 0.434377, 0.127482]  # Corresponding y-values
    })

    # Sort calibration curve by y-values for interpolation
    sorted_curve = calibration_curve.sort_values(by='y')

    # Step 1: Clean the test data from the file
    data = clean_data(file_name)
    data.columns = data.columns.str.strip()  # Remove any leading/trailing spaces
    print("Columns in the data:", data.columns)

    # Print the first few rows to understand the structure
    print("First few rows of the data:\n", data.head())

    # Ensure Total Average is numeric
    data['Total Average'] = pd.to_numeric(data['Total Average'], errors='coerce')

    # Drop rows where Total Average is NaN after conversion
    data = data.dropna(subset=['Total Average'])

    # Step 2: Interpolate and add the pH values as a new column
    data['Interpolated pH'] = data['Total Average'].apply(lambda y: interpolate_x(sorted_curve, y))

    # Save the updated data back to the file
    # Step 3: Save to a new file with an incremented name
    base_name, ext = os.path.splitext(file_name)
    i = 1
    while os.path.exists(f"{base_name}_{i}{ext}"):
        i += 1
    new_file_name = f"{base_name}_{i}{ext}"
    data.to_csv(new_file_name, index=False)
    print(f"Updated data saved to {new_file_name}")

    # Step 4: Delete the original buffer file
    os.remove("cleaned_data.csv")
    os.remove(file_name)
    print(f"Buffer file {file_name} deleted.")

    # Step 3: Plot test data
    fig, ax = plt.subplots()

    # Plot the calibration curve
    ax.plot(sorted_curve['x'], sorted_curve['y'], marker='o', color='blue', label='Calibration Curve')

    # Interpolate and plot data for each color
    for color in data['Color'].unique():
        color_data = data[data['Color'] == color]

        # Plot the interpolated values
        ax.plot(color_data['Interpolated pH'], color_data['Total Average'], marker='x', color='green',
                label=f'{color} Interpolated', linestyle='--')

    # Customize the plot
    ax.set_title('pH Sensor Test Results with Interpolation')
    ax.set_xlabel('pH Value')
    ax.set_ylabel('Percent of Total Light')
    ax.legend(title='Color')

    # Show the plot
    plt.show()



def send_command_to_pico(command):
    pico_serial = serial.Serial('COM3', 115200, timeout=0.1)  # Longer timeout
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
    pico_serial = serial.Serial('COM3', 115200, timeout=1)  # Adjust as needed
    time.sleep(2)  # Allow Pico to initialize

    # Send the command to the Pico
    pico_serial.write(command.encode() + b'\n')
    print(f"Sent command: {command}")

    with open(output_file, "w") as f:
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

draw_graph("data.csv")