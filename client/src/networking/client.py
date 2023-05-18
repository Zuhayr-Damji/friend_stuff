import asyncio
import websockets

serverUrl = "ws://" + "localhost:8000"

async def client():
    async with websockets.connect(serverUrl) as websocket:
        await websocket.send("Hello, server!")
        response = await websocket.recv()
        print(f"Received response: {response}")
        
asyncio.get_event_loop().run_until_complete(client())