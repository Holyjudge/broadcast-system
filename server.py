import asyncio
import websockets
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading

connected_clients = set()

async def handler(websocket):
    connected_clients.add(websocket)
    print(f"Client connected. Total: {len(connected_clients)}")

    try:
        async for message in websocket:
            print(f"Broadcasting: {message}")
            for client in connected_clients:
                await client.send(message)
    except websockets.exceptions.ConnectionClosedError:
        print("Client dropped unexpectedly.")
    finally:
        connected_clients.remove(websocket)
        print(f"Client disconnected. Total: {len(connected_clients)}")

def start_http_server():
    httpd = HTTPServer(("0.0.0.0", 8080), SimpleHTTPRequestHandler)
    print("HTTP server started on http://0.0.0.0:8080")
    httpd.serve_forever()

async def main():
    thread = threading.Thread(target=start_http_server, daemon=True)
    thread.start()

    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("WebSocket server started on ws://0.0.0.0:8765")
        await asyncio.Future()




if __name__ == "__main__":
    asyncio.run(main())

