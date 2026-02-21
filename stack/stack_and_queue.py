#STACK AND QUEUE


#STACK
from collections import deque
class Stack:
    def __init__(self):
        self.arr = deque()
    def push(self,x):
        self.arr.append(x)
    def pop(self):
        if self.is_empty():
            return None
        return self.arr.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.arr[-1]
    def is_empty(self):
        return len(self.arr) == 0



#QUEUE
class Queue:
    def __init__(self):
        self.arr = deque()
    def enqueue(self,x):
        self.arr.append(x)
    def dequeue(self):
        if self.is_empty():
            return None
        return self.arr.popleft()


    def front(self):
        if self.is_empty():
            return None
        return self.arr[0]
    def is_empty(self):
        return len(self.arr) == 0
