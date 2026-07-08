from time import sleep, ctime, time
import multiprocessing

# 1. ขั้นตอนต้อนรับหน้าร้าน ทำแบบ Synchronous เรียงทีละคน
def greet_diners(customer):
    print(f"{ctime()} Greeting for Customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")

# 2. กระบวนการด้านหลังของลูกค้าแต่ละคน ที่จะถูกนำไปรันแยกในเธรดของตัวเอง
def customer_private_workflow(customer):
    # Take Order
    print(f"{ctime()} [Thread-{customer}] Taking Order ...")
    sleep(1)
    print(f"{ctime()} [Thread-{customer}] Taking Order ...Done!")

    # Do Cooking
    print(f"{ctime()} [Thread-{customer}] Cooking Spaghetti ...")
    sleep(1)
    print(f"{ctime()} [Thread-{customer}] Cooking Spaghetti ...Done!")

    # Manage Bar
    print(f"{ctime()} [Thread-{customer}] Manage Bar for Drink ...")
    sleep(1)
    print(f"{ctime()} [Thread-{customer}] Manage Bar for Drink ...Done!")
    print(f"{ctime()} [Thread-{customer}] All served!\n")


if __name__ == "__main__":
    customers = ['A', 'B', 'C']
    start_time = time()
    
# ----------------------------------------------------------
# PHASE 1: Greet ลูกค้าทีละคนแบบ Synchronous (เข้าใจชื่อก่อนลงสั่งงาน)
# ----------------------------------------------------------

    for customer in customers:
        greet_diners(customer)

    print(f"\n{ctime()} === All customers greeted. Splitting into individual workflows ===\n")


    processes = []
    for customer in customers:
     p = multiprocessing.Process(target=customer_private_workflow, args=(customer,))
     processes.append(p)
     p.start()

    for p in processes:
        p.join()
    
    duration = time() - start_time
    print(f"{ctime()} Finished Entire Restaurant Operation in {duration:.2f} seconds")