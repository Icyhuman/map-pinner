import asyncio
import websockets
import os


async def echo(websocket):
    async for message in websocket:
        command=message.split(',')[0]
        if command=='images':
            message=listfiles()
            await websocket.send(message)
        if command=='pin':
            savepin(message)

        print(message)
        #await websocket.send(message)


async def main():
    async with websockets.serve(echo, "localhost", 8008) as server:
        print('Fuck')
        await server.serve_forever()

def listfiles():
    string=''
    if 'pins.txt' in os.listdir():
        string='resMyCoolSeparator'
    imglist=os.listdir('screenshots')
    for name in imglist:
        string=string+'screenshots/'+name+','
    string=string[:-1]
    if 'pins.txt' in os.listdir():
        string=string+'MyCoolSeparator'
        with open('pins.txt', 'r') as file:
            for line in file.readlines():
                data=line.split(',')
                string=string+data[0]+'  '+data[1]+','
        string=string[:-1]

    
    return string

def savepin(data):
    with open('pins.txt', 'a') as file:
        file.write(data[4:]+'\n')

if __name__ == "__main__":

    asyncio.run(main())

