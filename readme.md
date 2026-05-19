# Broadcast Server

A real-time broadcast messaging system built with Python WebSockets. Supports a CLI client and a browser-based chat UI.

## Features

- Real-time message broadcasting to all connected clients
- CLI interface to start the server or connect as a client
- Browser-based chat UI — no install needed on the client side
- Multi-device support over local network
- Graceful handling of client disconnections

## Project Structure

broadcast-server/
├── server.py        # WebSocket server + HTTP file server
├── client.py        # Terminal-based WebSocket client
├── cli.py           # CLI entry point
├── index.html       # Browser-based chat UI
├── requirements.txt
└── README.md

## Requirements

- Python 3.10+
- websockets

## Installation

git clone https://github.com/Holyjudge/broadcast-system
cd broadcast-system
pip install -r requirements.txt

## Usage

### Start the server

python cli.py start

Server listens for WebSocket connections on port `8765` and serves the chat UI over HTTP on port `8080`.

### Connect via terminal

python cli.py connect

### Connect via browser

Open `http://localhost:8080/index.html` in your browser.

## Multi-device Usage (Local Network)

1. Find your local IP address:

ipconfig       # Windows
ifconfig       # macOS/Linux

2. Update the WebSocket URL in `index.html`:

const ws = new WebSocket("ws://YOUR_IP:8765");

3. Start the server:

python cli.py start

4. On any device connected to the same network, visit:

http://YOUR_IP:8080/index.html

## How It Works

- The server maintains a set of all active WebSocket connections
- When a message arrives from any client, it is broadcast to all connected clients including the sender
- The browser UI uses the native WebSocket API — no libraries needed
- The terminal client uses `asyncio.to_thread` to handle simultaneous input and output without blocking

## Tech Stack

- Python `websockets` — WebSocket server and client
- Python `asyncio` — async event loop for concurrent client handling
- Python `http.server` — serves the chat UI over HTTP
- React (via CDN) — browser UI
- Tailwind CSS (via CDN) — styling

- Project URL: https://github.com/Holyjudge/broadcast-system
