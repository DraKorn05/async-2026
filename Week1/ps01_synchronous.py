from time import sleep, ctime, time, process_time
import os
import threading
import psutil

# ฟังก์ชันของการทำงานให้ลูกค้า 1 คนแบบซิงโครนัส
def make_coffee(customer_name):
    # ดึง PID และ Thread ID ออกมาดู
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(
        f"{ctime()} | [PID: {pid}] [TID: {thread_id}] "
        f"[Thread Name: {thread_name}] กำลังชงกาแฟให้ ลูกค้า {customer_name}..."
    )

    # จำลองงานหนัก CPU-bound
    sum(i * i for i in range(10000000))

    sleep(5)  # จำลองการทำงาน I/O

    print(
        f"{ctime()} | [PID: {pid}] [TID: {thread_id}] "
        f"[Thread Name: {thread_name}] ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!"
    )

def main():
    queue = ['A', 'B', 'C']

    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(
        f"{ctime()} | [Main PID: {main_pid}] [Main TID: {main_tid}] "
        f"=== เริ่มระบบจำลองตู้กาแฟแบบ Synchronous ==="
    )

    start_time = time()
    start_cpu = process_time()  # เริ่มจับเวลา CPU

    # ทำงานตามลำดับทีละคน
    for customer in queue:
        make_coffee(customer)

    duration = time() - start_time
    cpu_duration = process_time() - start_cpu

    # วัดการใช้ RAM
    process = psutil.Process(os.getpid())
    mem_mb = process.memory_info().rss / (1024 * 1024)

    print("\n[ข้อมูล Synchronous]")
    print(f"เวลาใช้งานจริง (Wall Time): {duration:.2f} วินาที")
    print(f"เวลาที่ CPU ใช้ประมวลผล (CPU Time): {cpu_duration:.4f} วินาที")
    print(f"หน่วยความจำ Memory (RAM) ที่ใช้: {mem_mb:.2f} MB")

if __name__ == "__main__":
    main()