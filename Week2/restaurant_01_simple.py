import asyncio
from time import ctime, sleep,time

def greeting(customer):
    print(f"{ctime()} | Greeting customer {customer}...")
    sleep(1)
    print(f"{ctime()} | Done greeting customer {customer}.")


def take_order(customer):
    print(f"{ctime()} | Taking order for {customer}...")
    sleep(1)
    print(f"{ctime()} | Done taking order for {customer}.")


def cook_food(customer):
    print(f"{ctime()} | Cooking food for {customer}...")
    sleep(1)
    print(f"{ctime()} | Done cooking food for {customer}.")


def bar(customer):
    print(f"{ctime()} | Bar is open for {customer}...")
    sleep(1)
    print(f"{ctime()} | Bar is closed for {customer}.")


if __name__ == "__main__":
    customers = ["A", "B", "C"]
    start_time = time()

    for customer in customers:
        greeting(customer)
        take_order(customer)
        cook_food(customer)
        bar(customer)

    duration = time() - start_time
    print(f"{ctime()} | Finished cooking is : {duration:0.2f} seconds")