# Program 8: Task Interleaving (Context Switching)
# Concept: Watching a single thread switch back and forth between two different workflows using create_task.

import asyncio
from time import time, ctime

async def kitchen_crew():
    print(f"{ctime()} | Kitchen crew starts preparing the meal...")
    await asyncio.sleep(1)  # Simulate a delay of 1 second
    print(f"{ctime()} | Kitchen crew finished preparing the meal.")
    
async def bar_crew():
    print(f"{ctime()} | Bar crew starts preparing the drinks...")
    await asyncio.sleep(1)  # Simulate a delay of 1 second
    print(f"{ctime()} | Bar crew finished preparing the drinks.")

async def main():
    start = time()

    # Create tasks for both crews
    task1 = asyncio.create_task(kitchen_crew())
    task2 = asyncio.create_task(bar_crew())

    # Wait for both tasks to complete
    await task1
    await task2

    print(f"Total Time: {time() - start:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine using the event loop