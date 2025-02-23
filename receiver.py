import asyncio
import websockets
import pyvjoy  # vJoy for virtual steering wheel

vjoy = pyvjoy.VJoyDevice(1)  # Connect to vJoy device

async def receive_gyro_data():
    server = await websockets.serve(handle_connection, "0.0.0.0", 8765)
    await server.wait_closed()

async def handle_connection(websocket, path):
    total_rotation = 0  # To track cumulative rotation
    async for message in websocket:
        gyro_x, gyro_y, gyro_z = map(float, message.split(','))

        total_rotation += gyro_z  # Track full turns
        steering_value = min(max(total_rotation / 900, -1), 1)  # Normalize (-1 to 1)

        vjoy.set_axis(pyvjoy.HID_USAGE_X, int(steering_value * 32767))  # Map to vJoy

asyncio.run(receive_gyro_data())
