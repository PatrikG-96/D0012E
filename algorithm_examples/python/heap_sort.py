
def right(i):
    return 2*i+2

def left(i):
    return 2*i+1

def max_heapify(arr, heap_size, i):
    l = left(i)
    r = right(i)
    largest = 0
    if l < heap_size and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        t = arr[i]
        arr[i] = arr[largest]
        arr[largest] = t
        max_heapify(arr, heap_size, largest)

def build_max_heap(arr):

    i = len(arr)//2
    while i >= 0:
        max_heapify(arr, len(arr), i)
        i-=1

def heap_sort(arr):
    build_max_heap(arr)
    i = len(arr)-1
    size = len(arr)
    while i > 0:
        t = arr[0]
        arr[0] = arr[i]
        arr[i] = t
        size -= 1
        i-=1
        max_heapify(arr, size, 0)

        
        

lst = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
heap_sort(lst)
print(lst)
