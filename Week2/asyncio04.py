# Program 4: The await Keyword
# Concept: Pausing a coroutine to let another operation finish using await.
import asyncio
from time import ctime

async def greet():
    print(f"{ctime()} -> Task Started")

    await asyncio.sleep(1)

    print(f"{ctime()} -> Task Finished")

if __name__ =="__main__":
    asyncio.run(greet())