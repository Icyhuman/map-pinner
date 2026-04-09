import asyncio
import websockets


async def echo(websocket):
    x=0
    async for message in websocket:
        print(x)
        x+=1
        print(message)
        await websocket.send(message)


async def main():
    async with websockets.serve(echo, "localhost", 8008) as server:
        print('Fuck')
        await server.serve_forever()


if __name__ == "__main__":
    x=0
    asyncio.run(main())