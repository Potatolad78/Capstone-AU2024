import serial 
import time 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x_calibration = np.array([5,7,9.5])
y_calibration = np.array([0.8492741896,  0.6989145363, 0.3558160278])

sorted_indices = np.argsort(y_calibration)
x_calibration_sorted = x_calibration[sorted_indices]
y_calibration_sorted = y_calibration[sorted_indices]

def interpolate_x(x_values, y_values, target_y):
    for i in range(len(y_values) - 1):
        if (y_values[i] <= target_y <= y_values[i + 1]) or (y_values[i] >= target_y >= y_values[i + 1]):
            x1, x2 = x_values[i], x_values[i + 1]
            y1, y2 = y_values[i], y_values[i + 1]
            target_x = x1 + (target_y - y1) * (x2 - x1) / (y2 - y1)
            return target_x
    return None  # If the y-value is out of range


def communicate_with_pico():

    pico_serial = serial.Serial('COM3', 115200, timeout=1)
    time.sleep(2)

    pico_serial.write(b'collect_data\n')
    time.sleep(10)
    csv_data = pico_serial.read_all.decode('utf-8')
    pico_serial.close()
    with open("pico_data.cv", "w") as f:
        f.write(csv_data)
    
    return 'pico_data.csv'

def process_csv_data(csv_file):
    df = pd.read_csv(csv_file)
    x_new_data = df['X_Value']  # Replace with the correct column name in the CSV for X values
    y_new_data = df['Y_Value']  # Replace with the correct column name in the CSV for Y values
    return x_new_data, y_new_data


def plot_data():
    # Load the data from the CSV file
    x_new_data, y_new_data = process_csv_data('pico_data.csv')

    # Interpolate new X values from the given Y values
    interpolated_x = [interpolate_x(x_calibration_sorted, y_calibration_sorted, y) for y in y_new_data]
    
    # Plot the calibration curve (line going through all points)
    plt.plot(x_calibration_sorted, y_calibration_sorted, marker='o', color='blue', label='Calibration Curve')

    # Plot the new data points from the CSV file
    plt.scatter(x_new_data, y_new_data, color='red', label='CSV Data Points')

    # Plot the interpolated points
    for i, y_new in enumerate(y_new_data):
        plt.scatter(interpolated_x[i], y_new, color='green', label=f'Interpolated Point ({interpolated_x[i]:.2f}, {y_new})')

    # Add labels and title
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Calibration Curve with Interpolated Data Points')
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function
def main():
    # Step 1: Send command to Pico and collect data
    print("Sending command to Pico...")
    communicate_with_pico()

    # Step 2: Plot the data and calibration curve
    print("Plotting data...")
    plot_data()
