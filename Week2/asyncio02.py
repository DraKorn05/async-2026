# Program 2: The Coroutine Object
# Concept: Seeing that calling an async def function creates an "Object" but does not execute it yet.

import asyncio

async def greet():
    print
    
coro_object = greet()  # Calling the async function creates a coroutine object but does not execute it yet.

print(type(coro_object))  # This will print <class 'coroutine'>, indicating that coro_object is a coroutine object.