async func could be await-ed in jupyter lab directly:

```py
import asyncio
import websockets
import datetime

async def attach(uri, n=5):
    data = []
    async with websockets.connect(uri) as ws:
        for i in range(n):
            recv = await ws.recv()
            print(recv)
            data.append(recv)
    return data

data = await attach(endpoint)
len(data)
```
