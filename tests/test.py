import asyncio
import time as tim


async def notify():
    while True:
        print(f"Now: {tim.strftime('%X')}         ", end="\r")
        await asyncio.sleep(1)

async def Ex():
    while True:
        print("Visite nosso site...", end="\r")
        await asyncio.sleep(2)
        print("www.like.com.br", end="\r")
        await asyncio.sleep(5)

async def main():
    other = asyncio.create_task(Ex())
    clock = asyncio.create_task(notify())

    await other
    await clock

asyncio.run(main())
