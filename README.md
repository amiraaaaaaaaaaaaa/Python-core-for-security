# python-core-for-security

This repository contains implementations of two fundamental data structures in Python: **Stack** and **Queue**.  
These are implemented from scratch using Python's `collections.deque`, which ensures efficient operations.

---

## 📁 Implemented Data Structures

### 1. Stack
- **Description:**  
  Stack is a **LIFO (Last In, First Out)** data structure.  
  Elements are added and removed only from the top.  

- **Operations:**
  - `push(x)` → add element to the top  
  - `pop()` → remove and return the top element  
  - `peek()` → view the top element without removing it  
  - `is_empty()` → check if the stack is empty  

- **Time Complexity:**
  - `push` → O(1)  
  - `pop` → O(1)  
  - `peek` → O(1)  

- **Security Applications:**
  - Call stack analysis and stack overflow detection  
  - Reversing payloads in exploit development  
  - Parsing expressions, brackets, or code for static analysis  
  - Backtracking algorithms in penetration testing  

---

### 2. Queue
- **Description:**  
  Queue is a **FIFO (First In, First Out)** data structure.  
  Elements are added at the rear and removed from the front.  

- **Operations:**
  - `enqueue(x)` → add element to the rear  
  - `dequeue()` → remove and return the front element  
  - `front()` → view the first element without removing it  
  - `is_empty()` → check if the queue is empty  

- **Time Complexity:**
  - `enqueue` → O(1)  
  - `dequeue` → O(1)  
  - `front` → O(1)  

- **Security Applications:**
  - Network packet processing and buffering  
  - Rate limiting and preventing DDoS attacks  
  - BFS algorithms for network or graph analysis  
  - Task scheduling in automated security scripts  

---

## 📌 Example Usage

```python
# Stack example
s = Stack()
s.push(10)
s.push(20)
print(s.peek())  # 20
s.pop()
print(s.peek())  # 10

# Queue example
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.front())  # 1
q.dequeue()
print(q.front())  # 2