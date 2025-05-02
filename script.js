const accelSpan = document.getElementById("accel");
const gyroSpan = document.getElementById("gyro");

async function fetchIMUData() {
  try {
    const response = await fetch("http://127.0.0.1:8000/imu");
    const data = await response.json();
    accelSpan.textContent = `X: ${data.ax}, Y: ${data.ay}, Z: ${data.az}`;
    gyroSpan.textContent = `X: ${data.gx}, Y: ${data.gy}, Z: ${data.gz}`;
  } catch (err) {
    accelSpan.textContent = "Error fetching data";
    gyroSpan.textContent = "";
  }
}

setInterval(fetchIMUData, 1000); // fetch every 1 second
