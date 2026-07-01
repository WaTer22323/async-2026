# Program 10: Extracting Return Values from Tasks
# Concept: Accessing returned results from completed Task objects using .result() or direct assignment.
import asyncio
from time import ctime, time

async def calculate_bill(customer, base_price):
    print(f"Calculating bill for {customer}...")
    await asyncio.sleep(1)  # Simulate a delay in calculation
    final_price = base_price * 1.07  # Adding a 20% service charge
    return final_price

async def main():
    task_a = asyncio.create_task(calculate_bill("A", 100))
    task_b = asyncio.create_task(calculate_bill("B", 200))

    result_a = await task_a  # Wait for task_a to complete and get the result
    result_b = await task_b  # Wait for task_b to complete and get the result

    print(f"Final bill for customer A: ${result_a:.2f}")
    print(f"Final bill for customer B: ${result_b:.2f}")    
    print(f"Total bill: ${result_a + result_b:.2f}")

if __name__ == "__main__":
    asyncio.run(main())