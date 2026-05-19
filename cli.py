import argparse
import asyncio
from server import main
from client import connect

def run():
    parser = argparse.ArgumentParser(description="Broadcast Server CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("start", help="Start the broadcast server")
    subparsers.add_parser("connect", help="Connect to the broadcast server")

    args = parser.parse_args()

    if args.command == "start":
        asyncio.run(main())

    elif args.command == "connect":
        try:
            asyncio.run(connect())
        except KeyboardInterrupt:
            print("\nDisconnected!!")
    else:
        parser.print_help()


if __name__ == "__main__":
    run()
