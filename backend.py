import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        print(message)
        await websocket.send(message)


async def main():
    async with websockets.serve(echo, "localhost", 8008) as server:
        print('Fuck')
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())