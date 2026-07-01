# Program 9: Dynamically Tracking Tasks in a List
# Concept: Managing multiple generated tasks dynamically by appending them into a standard Python list.
import asyncio
from time import ctime, time

async def serve_customer(name):
    print(f"{ctime()} -> Handling Customer {name}...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> Done {name}!")
async def main():
    start_time = time()
    customers = ["A", "B", "C", "D", "E"]
    tasks = []

    for name in customers:
        t = asyncio.create_task(serve_customer(name))
        tasks.append(t)

    for t in tasks:
        await t

    print(f"served {len(customers)} customers in {time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
