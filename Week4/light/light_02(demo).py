# light_01_sequential_on.py

import asyncio
from time import time, ctime
from light_utils import control_light, reset_lights

MY_STUDENT_ID = "6710301012"

# ลำดับไฟที่ต้องเปิดเรียงกัน ห้ามสลับ และห้ามเปิดดวงถัดไปก่อนดวงก่อนหน้าจะติดเสร็จ
LIGHT_SEQUENCE = ["light_1", "light_2", "light_3", "light_4"]


async def main():
    print(
        f"{ctime()} | --- [Sequential] Turning on lights in strict order "
        f"({' -> '.join(LIGHT_SEQUENCE)}) ---"
    )

    # เคลียร์สถานะไฟทั้งหมดกลับเป็น OFF ก่อนเริ่มทุกครั้ง
    await reset_lights(MY_STUDENT_ID)

    start_time = time()

    # หัวใจของโจทย์นี้คือ "await ทีละดวง" ไม่ใช่ create_task + gather
    # เพราะถ้าใช้ create_task/gather ทั้ง 4 ดวงจะถูกยิงพร้อมกันทันที (concurrent)
    # ซึ่งจะทำให้ไฟติดไม่เรียงลำดับตามที่โจทย์ต้องการ (ลำดับจริงจะขึ้นกับว่าดวงไหนดีเลย์น้อยสุด)
    #
    # การ await ตรงๆ ในลูปแบบนี้ จะบังคับให้ event loop รอผลลัพธ์ของ
    # ไฟดวงปัจจุบันให้เสร็จสมบูรณ์ก่อน แล้วค่อยเริ่มยิงคำขอของดวงถัดไป
    # -> รับประกันว่าไฟจะติดเรียงตามลำดับ 1 -> 2 -> 3 -> 4 เสมอ ไม่ว่า delay ของแต่ละดวงจะต่างกันแค่ไหน
    for light_id in LIGHT_SEQUENCE:
        result = await control_light(MY_STUDENT_ID, light_id, "ON")

        if result.get("status") == "ERROR":
            print(f"{ctime()} | [FAILED] {light_id} -> {result['detail']}")
            continue

        elapsed_so_far = time() - start_time
        print(
            f"{ctime()} | [ON] {result['light_id']} is now "
            f"{result['current_status']} "
            f"(elapsed so far: {elapsed_so_far:.2f}s)"
        )

    total_time = time() - start_time
    print(
        f"{ctime()} | All lights turned on sequentially. "
        f"Total time: {total_time:.2f} seconds "
        f"(sum of all 4 delays: 0.5 + 1.2 + 2.0 + 0.8 = 4.5s)."
    )


if __name__ == "__main__":
    asyncio.run(main())