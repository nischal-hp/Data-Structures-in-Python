# 1) Using List as a Stack
s = []
s.append('https://www.cnn.com/')  # To add element to Stack
s.append('https://www.cnn.com/world')

s.pop() # To remove element from Stack
s[-1] # To get just the last element from Stack

# 2) Using deque as a Stack
from collections import deque
stack = deque()
dir(stack) # Gives list of possible operations on stack

stack.append("https://www.cnn.com/")
stack.append('https://www.cnn.com/world')
stack.pop()

# 3) Implement Stack class using a deque as its internal data structure
class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

s = Stack()
s.push(5)
s.pop()