from collections import deque
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