from collections import deque
from threading import Thread
import time

#============================STACK=======================#
class Stack:
    def __init__(self):
        self.container = deque()
        
    def push(self, val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
    
  #=====================QUEUE========================#  
class Queue:
    def __init__(self):
        self.buffer = deque()
        
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return
        
        return self.buffer.pop()    
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
food_order_queue = Queue()

def place_orders(orders):
    for order in orders:
        print("placing order for:" , order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)
        
def serve_orders():
    time.sleep(1)
    while food_order_queue.size() > 0:
        order = food_order_queue.dequeue()
        print("Now serving: ", order)
        time.sleep(2)
    
orders = ['pizza','samosa','pasta','biryani','burger']

# thread1 = Thread(target=place_orders, args=(orders,))
# thread2 = Thread(target=serve_orders, )


# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# print("done")
    
# elts = deque()
# elts.extend([1,2,3,4,5,6,7,8])
# print(elts)
# elts.rotate(1)
# print(elts)

#=============================EXERCISE 2==============================#
b_number = Queue()
#TODO:1. WE ADD 1 TO THE QUEUE
b_number.enqueue("1")
print(b_number)
#TODO:2. THEN WE POP ALL THE QUEUE ELEMENTS AND ADD 1 AND 0 TO THEM
for i in range(10):
    num = b_number.dequeue()
    print(num)
    b_number.enqueue(num + "0")
    b_number.enqueue(num + "1")
    

#TODO:3 THEN ENQUEUE THE NEW ONES TO THE QUEUE

