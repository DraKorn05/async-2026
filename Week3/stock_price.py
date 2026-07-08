# นักเรียนต้องเลือกใช้ asyncio.wait() พร้อมออปชัน return_when=asyncio.FIRST_COMPLETED เท่านั้น (หากใครใช้ gather หรือ wait_for จะไม่ตรงสเปกเงื่อนไขการแข่งส่งข้อมูล)
# Objective: Implement complex processing workflows based on task fulfillment conditions.
import asyncio
from time import ctime

async def fetch_stock_price(server_name, delay):
    await asyncio.sleep(delay)
    return f"[{server_name}] Price: 150 USD"

async def main():
    # 
    tasks = {
        asyncio.create_task(fetch_stock_price("Alpha", 3.0)),
        asyncio.create_task(fetch_stock_price("Beta", 0.8)),
        asyncio.create_task(fetch_stock_price("Gamma", 1.5))
    }
    
    # 
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    #print(f"{ctime()} Count of Tasks Done: {len(done)}")       # 
    #print(f"{ctime()} Count of Tasks Pending: {len(pending)}") # 
    
    for finished_task in done:
        print(f"{ctime()} Winner Result: {finished_task.result()}")
        
    print(f"{ctime()} Cleaning up {len(pending)} pending tasks...")
        
    # 
    for ongoing_task in pending:
        ongoing_task.cancel()

asyncio.run(main())