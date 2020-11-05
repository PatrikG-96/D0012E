
class Heap:

    def __init__(self, max_size, arr = None):
        if arr==None and max_size:
            self.max_size = max_size
            self.heap = [0] * max_size
            self.heap_size = 0
        else:
            self.max_size = len(arr)
            self.heap_size = self.max_size
            self.heap = arr

            i = self.max_size//2
            while i >= 0:
                self.max_heapify(i)
                i-=1

    def insert(self, v):
        if self.heap_size == self.max_size:
            return
        self.heap[self.heap_size] = v
        self.insert_sort(v, self.heap_size)
        self.heap_size += 1
        
    def insert_sort(self, val, i):

        p = i//2
        p_val = self.heap[p]

        if val > p_val:
            self.heap[p] = val
            self.heap[i] = p_val
            self.insert_sort(val, p)

    def delete_max(self):
        self.heap[0] = self.heap[self.heap_size-1]
        self.heap_size -= 1
        self.max_heapify(0)
       
        
    def max_heapify(self, i):
        l = 2*i + 1
        r = 2*i + 2
        largest = 0
        if l < self.heap_size and self.heap[l] > self.heap[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and self.heap[r] > self.heap[largest]:
            largest = r
        if largest!=i:
            t = self.heap[i]
            self.heap[i] = self.heap[largest]
            self.heap[largest] = t
            self.max_heapify(largest)

    def get_max(self):
        return self.heap[0]

    def size(self):
        return self.heap_size

    def heap_as_array(self):
        return self.heap

    def print(self):
        print(self.heap)


h = Heap(10)

h.insert(10)
h.insert(5)
h.insert(11)
h.insert(15)
h.insert(3)
h.insert(7)
h.insert(60)
h.insert(9)
h.insert(1)
h.insert(77)
h.print()


  

lst = [1,9,3,77,60,15,11,5,10,7]

h2 = Heap(0, lst)
h2.print()
