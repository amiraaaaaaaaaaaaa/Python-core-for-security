
class Stack:
    def __init__(self):
        self.arr = []

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