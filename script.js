const BACKEND_URL = "https://hackerthon-1-72ma.onrender.com/imu"; // Your backend URL

async function fetchIMUData() {
  try {
    const res = await fetch(BACKEND_URL);
    if (!res.ok) throw new Error("Failed to fetch");

    const data = await res.json();

    // IMU Data
    document.getElementById("ax").textContent = data.imu.ax.toFixed(2);
    document.getElementById("ay").textContent = data.imu.ay.toFixed(2);
    document.getElementById("az").textContent = data.imu.az.toFixed(2);

    document.getElementById("gx").textContent = data.imu.gx.toFixed(2);
    document.getElementById("gy").textContent = data.imu.gy.toFixed(2);
    document.getElementById("gz").textContent = data.imu.gz.toFixed(2);

    document.getElementById("mx").textContent = data.imu.mx.toFixed(2);
    document.getElementById("my").textContent = data.imu.my.toFixed(2);
    document.getElementById("mz").textContent = data.imu.mz.toFixed(2);

    // GPS Data
    document.getElementById("lat").textContent = data.gps.lat.toFixed(7);
    document.getElementById("lon").textContent = data.gps.lon.toFixed(7);
    document.getElementById("alt").textContent = data.gps.alt.toFixed(2);

    document.getElementById("status").textContent = "✅ Live data updated.";
  } catch (err) {
    console.error(err);
    document.getElementById("status").textContent = "❌ Unable to connect.";
  }
}

setInterval(fetchIMUData, 1000); // Poll every second
