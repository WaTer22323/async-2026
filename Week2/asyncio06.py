# Program 6: Creating a Concurrent Task
# Concept: Wrapping a coroutine inside asyncio.create_task() to schedule it to run in the background.
import asyncio
from time import ctime,time

async def cook_spaghetti(customer):
    print(f"{ctime()} -> Starting cooking for customer {customer}...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> Finished cooking for customer {customer}!")

async def main():
    start_time = time( )

    task_a = asyncio.create_task(cook_spaghetti("A"))


    print(f"{ctime()}")

    await task_a  # Wait for the task to complete


    print(f"Total time: {time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())