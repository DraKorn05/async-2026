import asyncio
import time


def log(message: str) -> None:
    """Print a message prefixed with a human-readable timestamp."""
    print(f"{time.ctime()}  {message}")


async def greet_customer(name: str) -> None:
    """Greeting is done one at a time, in order (sequential await)."""
    log(f"Greeting for {name} ...")
    await asyncio.sleep(1)
    log(f"Greeting for {name} ...Done!")


async def customer_flow(name: str) -> None:
    """
    Each customer's full order flow runs as an independent async task.
    While one task is 'waiting' (e.g. spaghetti cooking), the single
    worker (event loop) switches to progress another task.
    """
    log(f"  [{name}] Taking Order ...")
    await asyncio.sleep(1)
    log(f"  [{name}] Taking Order ...Done!")

    log(f"  [{name}] Cooking Spaghetti ...")
    await asyncio.sleep(1)
    log(f"  [{name}] Cooking Spaghetti ...Done!")

    log(f"  [{name}] Manage Bar for Drink ...")
    await asyncio.sleep(1)
    log(f"  [{name}] Manage Bar for Drink ...Done!")

    log(f"  [{name}] All served!")


async def main() -> None:
    start = time.perf_counter()

    # Step 1: greet each customer one at a time (sequential)
    for name in ["Customer-A", "Customer-B", "Customer-C"]:
        await greet_customer(name)

    print()
    log("--- All customers greeted. Scheduling independent Async Tasks! ---")
    print()

    # Step 2: run each customer's full flow concurrently as independent tasks
    tasks = [
        asyncio.create_task(customer_flow(name), name=name)
        for name in ["Task-A", "Task-B", "Task-C"]
    ]
    await asyncio.gather(*tasks)

    elapsed = time.perf_counter() - start
    print()
    log(f"Finished Entire Restaurant Operation in {elapsed:.2f} seconds.")


if __name__ == "__main__":
    asyncio.run(main())