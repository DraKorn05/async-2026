from time import sleep, ctime, time
import multiprocessing
import threading
import os

# ฟังก์ชันจะทำงานแยกให้ลูกค้า 1 คน
def make_coffee(customer_name):
    # ดึง PID ของแต่ละโปรเซส
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(
        f"{ctime()} | [PID: {pid}] [TID: {thread_id}] "
        f"[Thread Name: {thread_name}] กำลังชงกาแฟให้ ลูกค้า {customer_name}..."
    )

    sleep(5)  # ใช้เวลา 5 วินาที

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
        f"=== เริ่มระบบจำลองตู้กาแฟแบบ Multi-processing ==="
    )

    start_time = time()

    processes = []

    # แยก process ให้ลูกค้าแต่ละคน
    for customer in queue:
        p = multiprocessing.Process(
            target=make_coffee,
            args=(customer,)
        )

        processes.append(p)
        p.start()

    # รอให้ทุก process ทำงานเสร็จ
    for p in processes:
        p.join()

    duration = time() - start_time

    print(f"{ctime()} | ใช้เวลารวมทั้งหมด: {duration:.2f} วินาที")

if __name__ == "__main__":
    main()