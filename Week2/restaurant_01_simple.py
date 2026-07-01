import asyncio
from time import sleep,time, ctime

#greeting customers synchronously
def greet_customer(costomer):
    print(f"{ctime()} | Greeting for customer: {costomer}")
    # Simulate time taken to greet customer
    sleep(1)
    print(f"{ctime()} | Finished greeting customer: {costomer}")
    
def take_order(costomer):
    print(f"{ctime()} | Taking order from customer: {costomer}")
    # Simulate time taken to take order
    sleep(1)
    print(f"{ctime()} | Finished taking order from customer: {costomer}")

def do_cooking(costomer):
    print(f"{ctime()} | Cooking order for customer: {costomer}")
    # Simulate time taken to cook order 
    sleep(1)
    print(f"{ctime()} | Finished cooking order for customer: {costomer}")
    
def mini_bar(costomer):
    print(f"{ctime()} | Serving mini bar to customer: {costomer}")
    # Simulate time taken to serve mini bar 
    sleep(1)
    print(f"{ctime()} | Finished serving mini bar to customer: {costomer}")
    
if __name__ == "__main__":
    
    customers = ["A, B, C"]
    start = time()
    
    for customer in customers:
        greet_customer(customer)
        take_order(customer)
        do_cooking(customer)
        mini_bar(customer)
        
    duration = time() - start
    print(f"{ctime()} | Finished in: {duration:.2f} seconds")