import asyncio
import websockets
import os


async def echo(websocket):
    async for message in websocket:
        command=message.split(',')[0]
        if command=='images':
            message=listfiles()
            await websocket.send(message)

        print(message)
        #await websocket.send(message)


async def main():
    async with websockets.serve(echo, "localhost", 8008) as server:
        print('Fuck')
        await server.serve_forever()

def listfiles():
    imglist=os.listdir('screenshots')
    string=''
    for name in imglist:
        string=string+'screenshots/'+name+','

    
    return string[:-1]


if __name__ == "__main__":
    x=0
    #listfiles()
    asyncio.run(main())

