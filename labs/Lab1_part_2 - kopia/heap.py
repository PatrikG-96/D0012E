import sys

class Element:

        def __init__(self, data, w):
            self.data = data
            self.w = w

class MinHeap:

    def __init__(self, size):
        self.heap = [None] * size
        self.max_size = size
        self.heap_size = 0
        self.indices = [-1] * size
        self.heap[0] = Element(None, sys.maxsize)

    def insert(self, item, weight):
        if self.heap_size >= self.max_size:
            return
        e = Element(item, weight)
        self.indices[item] = self.heap_size
        self.heap[self.heap_size] = e
        self.reverse_heapify(e, self.heap_size)
        self.heap_size += 1
       

    def extract_min(self):
        if self.heap_size > 0:
            temp = self.heap[0]
            self.heap[0] = self.heap[self.heap_size-1]
            self.min_heapify(0)
            self.heap_size -= 1
            return (temp.data, temp.w)
        return None

    def decreaseWeight(self, vertex, weight):
        index = self.indices[vertex]
        element = self.heap[index]
        element.w = weight
        self.reverse_heapify(element, index)

    def reverse_heapify(self, e, i):
        parent = i // 2

        if self.heap[parent].w > e.w:
            temp = self.heap[parent]
            self.heap[parent] = e
            self.heap[i] = temp
            self.indices[e.data] = parent
            self.indices[temp.data] = i
            self.reverse_heapify(e, parent)

    def min_heapify(self, i):
        l = 2 * i + 1
        r = 2 * i + 2
        smallest = 0
        if l < self.heap_size and self.heap[i].w > self.heap[l].w:
            smallest = l
        else:
            smallest = i
        if r < self.heap_size and self.heap[smallest].w > self.heap[r].w:
            smallest = r
        if smallest != i:
            temp = self.heap[i]
            self.heap[i] = self.heap[smallest]
            self.heap[smallest] = temp
            self.indices[temp.data] = smallest
            self.indices[self.heap[i].data] = i
            self.min_heapify(smallest)

    def size(self):
        return self.heap_size


#############################################################################
    ################
    ########
    #
    #

class Heap_max:

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




class PriorityQueue:

    def __init__(self, max_size):
        self.max_size = max_size
        self.heap = [None] * max_size
        self.heap_size = 0
        self.heap[0] = Element(None, float('inf'))

    def push(self, data, w):
        if self.heap_size >= self.max_size:
            return
        e = Element(data, w)
        self.heap[self.heap_size] = e
        self.reverse_heapify(e, self.heap_size)
        self.heap_size += 1


    def reverse_heapify(self, e, i):
        parent = i // 2

        if self.heap[parent].w > e.w:
            temp = self.heap[parent]
            self.heap[parent] = e
            self.heap[i] = temp
            self.reverse_heapify(e, parent)
        
    def get_min(self):
        if self.heap_size > 0:
            return self.heap[0]
        return None

    def pop(self):
        if self.heap_size > 0:
            temp = self.heap[0]
            self.heap[0] = self.heap[self.heap_size-1]
            self.min_heapify(0)
            self.heap_size -= 1
            return (temp.data, temp.w)
        return None

    def print(self):
        print("[", end= "")
        for i in range(self.heap_size):
            print(self.heap[i].w, end = ", ")
        print("]")

    def size(self):
        return self.heap_size

    def min_heapify(self, i):
        l = 2 * i + 1
        r = 2 * i + 2
        smallest = 0
        if l < self.heap_size and self.heap[i].w > self.heap[l].w:
            smallest = l
        else:
            smallest = i
        if r < self.heap_size and self.heap[smallest].w > self.heap[r].w:
            smallest = r
        if smallest != i:
            temp = self.heap[i]
            self.heap[i] = self.heap[smallest]
            self.heap[smallest] = temp
            self.min_heapify(smallest)
    









        

        
