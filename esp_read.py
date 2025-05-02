import serial
import requests
import time

# Define the serial port and baud rate
SERIAL_PORT = 'COM10'  # Change this to your correct serial port (e.g., COM10 on Windows, /dev/ttyUSB0 on Linux/Mac)
BAUD_RATE = 115200  # Must match the baud rate of your ESP8266

# Backend URL
BACKEND_URL = 'https://hackerthon-1-72ma.onrender.com/imu'  # Replace with your actual backend URL

# Open serial port
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)

# Function to send data to the backend
def send_data_to_backend(data):
    try:
        response = requests.post(BACKEND_URL, json=data)
        if response.status_code == 200:
            print("Data successfully sent to backend!")
        else:
            print(f"Failed to send data to backend. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending data to backend: {e}")

# Main loop to read data from serial and send to backend
def main():
    while True:
        try:
            # Read the line from the serial monitor
            line = ser.readline().decode('utf-8').strip()

            if line:
                # Print raw data from ESP8266
                print(f"Received raw data: {line}")

                # Format the data into a dictionary
                # Assuming the data format is 'ax: -0.91, ay: -0.6, az: -1.86, gx: -80.21, gy: -211.59, gz: 70.1'
                data_dict = {}
                try:
                    # Split by commas and create a dictionary
                    for item in line.split(','):
                        key, value = item.split(':')
                        data_dict[key.strip()] = float(value.strip())

                    # Send data to backend
                    send_data_to_backend(data_dict)

                except Exception as e:
                    print(f"Error parsing data: {e}")

            # Wait for a while before reading the next data
            time.sleep(1)

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(1)

if __name__ == '__main__':
    main()
