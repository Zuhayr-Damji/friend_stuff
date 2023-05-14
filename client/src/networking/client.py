import asyncio
import websockets

async def client():
    async with websockets.connect("ws://localhost:8000") as websocket:
        await websocket.send("Hello, server!")
        response = await websocket.recv()
        print(f"Received response: {response}")
        
asyncio.get_event_loop().run_until_complete(client())
