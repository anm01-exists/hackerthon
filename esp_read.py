import serial
import time
import requests

# Update the port name with the correct COM port
SERIAL_PORT = 'COM10'  # Replace with your actual COM port (you can check it in Device Manager)
BAUD_RATE = 115200  # Make sure this matches the ESP8266 baud rate

# Backend URL where you want to send the data
BACKEND_URL = 'https://hackerthon-1-72ma.onrender.com/imu'  # Replace with your backend URL

def send_to_backend(data):
    try:
        response = requests.post(BACKEND_URL, json={"imu_data": data})
        if response.status_code == 200:
            print("Data successfully sent to backend!")
        else:
            print(f"Failed to send data to backend. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to backend: {e}")

def main():
    try:
        # Open the serial connection
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2) as ser:
            print(f"Connected to {SERIAL_PORT} at {BAUD_RATE} baud.")
            
            # Wait for some time to ensure ESP8266 is ready
            time.sleep(2)

            while True:
                # Read the serial data (a line of text)
                raw_line = ser.readline()

                # Check if raw_line is not empty
                if raw_line:
                    try:
                        # Attempt to decode the byte data to UTF-8, ignoring errors
                        line = raw_line.decode("utf-8", errors="ignore").strip()
                        print(f"Received: {line}")
                        
                        # Send data to backend
                        send_to_backend(line)

                    except UnicodeDecodeError as e:
                        print(f"Error decoding data: {e}")
                        print(f"Raw data: {raw_line}")
                else:
                    print("No data received or timeout reached.")

    except serial.SerialException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
