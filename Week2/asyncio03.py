# Program 3: The Event Loop (asyncio.run)
# Concept: Using the Event Loop to actually execute a Coroutine Object.

import asyncio

async def greet():
    print("Hello from Event Loop!")
    
if __name__ == "__main__":
    coro_object = greet()  # Create a coroutine object
    asyncio.run(coro_object)  # Run the coroutine object using the event loop