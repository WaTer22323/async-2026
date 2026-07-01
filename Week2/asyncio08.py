# Program 8: Task Interleaving (Context Switching)
# Concept: Watching a single thread switch back and forth between two different workflows using create_task.
import asyncio
from time import ctime, time

async def kitchen_crew():
    print(f"{ctime()} -> [Chef] puts noodles in boling water...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> [Chef] Starts the noodles")

async def bar_crew():
    print(f"{ctime()} -> [Bartender] starts grinding coffee beans...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> [Bartender] pour espresso shot!")

async def main():
    start_time = time()

    task_kitchen = asyncio.create_task(kitchen_crew())
    task_bar = asyncio.create_task(bar_crew())

    await task_kitchen  # Wait for the kitchen crew to finish
    await task_bar  # Wait for the bar crew to finish

    print(f"Total time: {time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())