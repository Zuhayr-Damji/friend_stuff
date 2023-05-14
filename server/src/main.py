import asyncio 
import websockets

async def server(websocket, path):
    message = await websocket.recv()
    print(f"Received message: {message}")
    await websocket.send("Thanks for the message!")

start_server = websockets.serve(server, "localhost", 8000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()