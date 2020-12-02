import sys
import heapq
from heap_sort import *

# Incremental design
def smallest3(arr):

    min1 = sys.maxsize
    min2 = sys.maxsize
    min3 = sys.maxsize

    for i in arr:
        if i < min1:
            min3 = min2
            min2 = min1
            min1 = i
        elif i < min2:
            min3 = min2
            min2 = i
        elif i < min3:
            min3 = i
    return [min1, min2, min3]

# Median of medians
def select(arr, i):

    if len(arr)==1:
        return arr[0]

    sub_lists = [arr[i:i+5] for i in range(0, len(arr), 5)]

    for lst in sub_lists:
        insertion_sort(lst)

    
    medians = [lst[len(lst)//2] for lst in sub_lists]

    
    if len(medians) > 5:
        m = select(medians, len(medians)//2)
    else:
        insertion_sort(medians)
        m = medians[len(medians)//2]

    #fixa bättre partitions
    low = [j for j in arr if j < m]
    high = [j for j in arr if j > m]
    
    k = len(low)

    if i < k:
        return select(low, i)
    elif i > k:
        return select(high, i-k-1)
    else:
        return m

#Divide and conquer design
def select_min_3(arr):
    pivot = select(arr, 2)

    min_lst = [i for i in arr if i <= pivot]
    insertion_sort(min_lst)
    return min_lst  

def insertion_sort(arr):
    for i in range(len(arr)):
        val = arr[i]
        j = i
        while i > 0 and val < arr[i-1]:
            swap(arr, i, i-1)
            i-=1

def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t
    



lst = [7,4,2,55,8,15,75,123,56]

print(select_min_3(lst))
print(smallest3(lst))
    

    
    
