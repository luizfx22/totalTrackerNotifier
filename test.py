import asyncio
import random

my_list = []

def cincoS():
    print("\n", "5 Segundos depois")

def notify(x):
    print("VALOR:", x, end="\r")


async def append_task():
    while True:
        await asyncio.sleep(5)        
        cincoS()


async def pop_task(a = 0):
    while True:        
        notify(a)
        a += 1
        await asyncio.sleep(0.01)


loop = asyncio.get_event_loop()
cors = asyncio.wait([append_task(), pop_task()])
loop.run_until_complete(cors)
