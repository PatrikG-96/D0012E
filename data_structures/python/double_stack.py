
#
# +---+---+---+---+---+---+-----+-----+
# | 0 | 1 | 2 | 3 | 4 | 5 | ... | n-1 |
# +---+---+---+---+---+---+-----+-----+
# ^                                   ^
# head 1 starts at -1                 head 2 starts at n
#
# If head 1 == head 2, array is full
# Stack 1 grows up, stack 2 grows down
# head 1 = -1 means empty stack 1, head 2 = n means empty stack 2

class DoubleStack:

    def __init__(self, size):
        self.size = size
        self.stack = [0] * size
        self.head1 = -1
        self.head2 = size


    def push1(self, v):
        if self.head1 == self.head2:
            print("full queue")
            return
        self.head1 += 1
        self.stack[self.head1] = v
        

    def pop1(self):
        if self.head1 == -1:
            print("empty queue")
            return
        r = self.stack[self.head1]
        self.head1 -= 1
        return r

    def push2(self, v):
        if self.head1 == self.head2:
            print("full queue")
            return
        self.head2 -= 1
        self.stack[self.head2] = v
       

    def pop2(self):
        if self.head2 == self.size:
            print("empty queue")
            return
        r = self.stack[self.head2]
        self.head2 += 1
        return r

    def print(self):
        print(self.stack)
        print("Stack 1 head is at: ", self.head1)
        print("Stack 2 head is at: ", self.head2)

q = DoubleStack(10)

q.push1(5)
q.push1(5)
q.push1(5)
q.push1(5)
q.push1(5)
q.print()
q.push2(4)
q.push2(4)
q.push2(4)
q.push2(4)
q.push2(4)
q.push2(4)
q.push2(4)
q.print()
q.pop1()
q.pop1()
q.push1(6)
q.push1(6)
q.print()
q.pop1()
q.pop2()
q.print()
q.pop1()
q.pop1()
q.pop1()
q.pop1()
q.pop1()
q.print()
q.pop2()
q.pop2()
q.pop2()
q.pop2()
q.pop2()
q.pop2()
q.print()
