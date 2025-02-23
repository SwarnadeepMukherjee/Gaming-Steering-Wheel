import asyncio
import websockets
import sensors

async def send_gyro_data():
    uri = "ws://<PC_IP>:8765"  # Replace with your PC's local IP
    async with websockets.connect(uri) as websocket:
        while True:
            gyro = sensors.get_gyroscope()  # Get gyro data
            data = f"{gyro[0]},{gyro[1]},{gyro[2]}"  # Format X, Y, Z
            await websocket.send(data)

asyncio.run(send_gyro_data())
