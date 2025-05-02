import time
import requests
import random

# Replace this with your actual backend URL
BACKEND_URL = "http://127.0.0.1:8000/imu"

def generate_fake_imu():
    return {
        "ax": round(random.uniform(-2, 2), 2),
        "ay": round(random.uniform(-2, 2), 2),
        "az": round(random.uniform(-2, 2), 2),
        "gx": round(random.uniform(-250, 250), 2),
        "gy": round(random.uniform(-250, 250), 2),
        "gz": round(random.uniform(-250, 250), 2)
    }

def send_imu_data():
    while True:
        data = generate_fake_imu()
        try:
            response = requests.post(BACKEND_URL, json=data)
            print(f"Sent: {data} | Response: {response.status_code}")
        except Exception as e:
            print(f"Failed to send data: {e}")
        time.sleep(1)

if __name__ == "__main__":
    send_imu_data()
