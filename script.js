const BACKEND_URL = "https://hackerthon-1-72ma.onrender.com/imu"; // Update this!

async function fetchIMUData() {
  try {
    const res = await fetch(BACKEND_URL);
    if (!res.ok) throw new Error("Failed to fetch");

    const data = await res.json();

    document.getElementById("ax").textContent = data.ax.toFixed(2);
    document.getElementById("ay").textContent = data.ay.toFixed(2);
    document.getElementById("az").textContent = data.az.toFixed(2);

    document.getElementById("gx").textContent = data.gx.toFixed(2);
    document.getElementById("gy").textContent = data.gy.toFixed(2);
    document.getElementById("gz").textContent = data.gz.toFixed(2);

    document.getElementById("mx").textContent = data.mx.toFixed(2);
    document.getElementById("my").textContent = data.my.toFixed(2);
    document.getElementById("mz").textContent = data.mz.toFixed(2);

    document.getElementById("status").textContent = "✅ Live data updated.";
  } catch (err) {
    console.error(err);
    document.getElementById("status").textContent = "❌ Unable to connect.";
  }
}

setInterval(fetchIMUData, 1000); // Poll every second
