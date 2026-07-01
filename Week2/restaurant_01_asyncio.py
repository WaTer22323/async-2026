import asyncio
from time import ctime, time


async def greet_dinner(customer):
    print(f"{ctime()} Greeting for Customer-{customer} ...")
    await asyncio.sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")


async def customer_private_workflow(customer):
    task_name = f"Task-{customer}"
    prefix = f"[{task_name}]"

    print(f"{ctime()} {prefix} Taking Order ...")
    await asyncio.sleep(1)
    print(f"{ctime()} {prefix} Taking Order ...Done!")

    print(f"{ctime()} {prefix} Cooking Spaghetti ...")
    await asyncio.sleep(1)
    print(f"{ctime()} {prefix} Cooking Spaghetti ...Done!")

    print(f"{ctime()} {prefix} Manage Bar for Drink ...")
    await asyncio.sleep(1)
    print(f"{ctime()} {prefix} Manage Bar for Drink ...Done!")

    print(f"{ctime()} {prefix} All served!")


async def main():
    customers = ["A", "B", "C"]
    start_time = time()

    for customer in customers:
        await greet_dinner(customer)

    print(f"\n{ctime()} --- All customer greeted. Scheduling independent Async tasks ---\n")

    tasks = [asyncio.create_task(customer_private_workflow(customer)) for customer in customers]
    await asyncio.gather(*tasks)

    duration = time() - start_time
    print(f"{ctime()} finished cooking in {duration:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
