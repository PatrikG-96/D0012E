
class Stack:

    def __init__(self, size):
        self.size = size
        self.stack = [0] * size
        self.head = 0

    def push(self, v):

        if self.head == self.size:
            print("full stack")
            return
        self.stack[self.head] = v
        self.head += 1

    def pop(self):

        if self.head == 0:
            print("empty stack")
            return
        self.head -= 1
        return self.stack[self.head]

    def isFull(self):
        return self.head == self.size

    def isEmpty(self):
        return self.head == 0

    def print(self):
        print(self.stack)


class Queue:

    def __init__(self, size):
        self.queue = Stack(size)
        self.dqueue = Stack(size)

    def enqueue(self, v):
        self.queue.push(v)

    def dequeue(self):
        if self.dqueue.isEmpty():
            while self.queue.isEmpty()==False:
                self.dqueue.push(self.queue.pop())
        return self.dqueue.pop()

    def print(self):
        print("queue: ")
        self.queue.print()
        print("dqueue: ")
        self.dqueue.print()

        

q = Queue(10)

for i in range(0,10):
    q.enqueue(i)

q.print()

for i in range(0,10):
    print(q.dequeue())

q.print()

q.dequeue()

q.enqueue(5)

q.print()

