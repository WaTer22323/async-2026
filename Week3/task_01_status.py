# Objective: Learn how to query the lifecycle status of a task object.
import asyncio
from time import ctime

async def short_job():
    await asyncio.sleep(1)
    return "Success"

async def main():
    task = asyncio.create_task(short_job())
    
    # Inspect status immediately while the task is still running
    print(f"{ctime()} Is task done? {task.done()}")          # Expect: False
    print(f"{ctime()} Is task canceled? {task.cancelled()}")  # Expect: False
    
    await task # wait for complete
    
    # Inspect status again after it finishes
    print(f"{ctime()} Is task done now? {task.done()}")      # Expect: True
    print(f"{ctime()} Is task canceled now? {task.cancelled()}") # Expect: False

asyncio.run(main())