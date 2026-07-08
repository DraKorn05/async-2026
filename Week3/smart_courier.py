# Delivery System): นักศึกษาต้องเขียน try...except CancelledError ได้ถูกต้อง 
# และใช้ .get_name(), .cancel(), และ .cancelled() ได้

import asyncio
from time import ctime


async def delivery_task(package_id, duration):
    """จำลองการส่งพัสดุด้วย asyncio.sleep(duration)"""
    print(f"{ctime()} Start delivering package {package_id} (ETA {duration}s)")
    await asyncio.sleep(duration)
    return f"Package {package_id} Delivered!"


async def main():
    # 2. สร้าง Task จาก delivery_task และตั้งชื่อว่า "Express-Courier"
    task = asyncio.create_task(
        delivery_task(package_id="P001", duration=5.0),
        name="Express-Courier"
    )

    try:
        # 3. ระหว่างพัสดุกำลังเดินทาง (ผ่านไป 2 วินาที) ตรวจสอบสถานะ
        await asyncio.sleep(2)
        print(f"{ctime()} Checking status of task: {task.get_name()}")
        print(f"{ctime()} Is '{task.get_name()}' done? {task.done()}")

        # 4. หากส่งของนานเกินไป (ผ่านไป 2 วินาทีแล้วยังไม่เสร็จ) ให้ยกเลิกงาน
        if not task.done():
            print(f"{ctime()} Delivery is taking too long! Cancelling '{task.get_name()}'...")
            task.cancel()

        # ต้อง await task เพื่อให้ CancelledError ถูกโยนขึ้นมาให้เราจับ
        result = await task
        print(f"{ctime()} Result: {result}")

    except asyncio.CancelledError:
        # 5. ดักจับ CancelledError
        print(f"{ctime()} Delivery Canceled! Returning package to warehouse.")
        print(f"{ctime()} Is '{task.get_name()}' cancelled now? {task.cancelled()}")


if __name__ == "__main__":
    asyncio.run(main())