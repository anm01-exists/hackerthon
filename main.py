from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with Netlify domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

imu_data = {
    "ax": 0, "ay": 0, "az": 0,
    "gx": 0, "gy": 0, "gz": 0
}

@app.post("/imu")
async def receive_imu(data: dict):
    global imu_data
    imu_data = data
    return {"message": "Data received"}

@app.get("/imu")
async def get_imu():
    return imu_data
