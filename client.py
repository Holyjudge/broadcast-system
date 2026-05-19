import asyncio
import websockets

async def connect():
    uri = "ws://YOUR_IP:8765"
    async with websockets.connect(uri) as websocket:
        print("Connected to server. Type your message and hit Enter.")
        print("Press Ctrl+C to disconnect.\n")

        async def receive():
            try:
                async for message in websocket:
                    print(f"\n<< {message}")
            except websockets.exceptions.ConnectionClosedOK:
                print("\nServer closed the connection.")
            except Exception as e:
                print(f"\nReceive error: {e}")

        async def send():
            try:
                while True:
                    message = await asyncio.to_thread(input, "You: ")
                    if message.strip():
                        await websocket.send(message.strip())
            except websockets.exceptions.ConnectionClosedOK:
                pass
            except Exception as e:
                print(f"\nSend error: {e}")

        await asyncio.gather(receive(), send())

if __name__ == "__main__":
    try:
        asyncio.run(connect())
    except KeyboardInterrupt:
        print("\nDisconnected.")