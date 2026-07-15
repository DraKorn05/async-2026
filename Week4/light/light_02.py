# light_02_concurrent_gather.py

import asyncio
from time import time, ctime
from light_utils import control_light, reset_lights

MY_STUDENT_ID = "6710301012"

LIGHT_IDS = ["light_1", "light_2", "light_3", "light_4"]


async def main():
    print(
        f"{ctime()} | --- [Concurrent] Turning on all lights "
        f"at the same time using create_task + gather ---"
    )

    # เคลียร์สถานะไฟทั้งหมดกลับเป็น OFF ก่อนเริ่มทุกครั้ง
    await reset_lights(MY_STUDENT_ID)

    start_time = time()

    # สร้าง task ทั้ง 4 ตัวพร้อมกันก่อน โดยยังไม่ await ทันที
    # เมื่อสร้างด้วย create_task() ทุกคำขอจะถูกส่งออกไปยัง event loop
    # และเริ่มทำงาน (ยิง HTTP request) แทบจะพร้อมกันทันที ไม่ต้องรอทีละดวง
    tasks = [
        asyncio.create_task(control_light(MY_STUDENT_ID, light_id, "ON"))
        for light_id in LIGHT_IDS
    ]

    # asyncio.gather รอให้ทุก task เสร็จพร้อมกัน
    # เวลารวมของทั้งชุดจะ "เท่ากับดวงที่ช้าที่สุด" (light_3 ดีเลย์ 2.0s)
    # ไม่ใช่ผลรวมของทุกดวงเหมือนแบบ sequential (0.5+1.2+2.0+0.8 = 4.5s)
    results = await asyncio.gather(*tasks)

    for result in results:
        if result.get("status") == "ERROR":
            print(f"{ctime()} | [FAILED] -> {result['detail']}")
            continue
        print(
            f"{ctime()} | [ON] {result['light_id']} is now "
            f"{result['current_status']}"
        )

    total_time = time() - start_time
    print(
        f"{ctime()} | All lights turned on concurrently. "
        f"Total time: {total_time:.2f} seconds "
        f"(should be ~2.0s, matching the slowest light: light_3)."
    )


if __name__ == "__main__":
    asyncio.run(main())