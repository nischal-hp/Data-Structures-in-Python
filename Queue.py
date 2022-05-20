# 1) Using List as a Queue
s = []
s.insert(0,131.10)  # To add element to Queue at the first position

s.pop() # To remove element from Queue. This wouldn't change compared to stack. Just the order in which elements are put into the array changes
s[-1] # To get just the last element from Queue

# 2) Using deque as a queue
from collections import deque
queue = deque()
dir(queue) # Gives list of possible operations on queue

queue.appendLeft("https://www.cnn.com/")
queue.appendLeft('https://www.cnn.com/world')
queue.pop()

# 3) Implement queue class using a deque as its internal data structure

from collections import deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})

pq.dequeue()