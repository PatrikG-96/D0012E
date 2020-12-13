

def min3(arr):
    
    min_elements = arr[0:3] #O(1)
    insertion_sort(min_elements)
    if len(arr) == 3:       #O(1)
        return min_elements
    
    for i in range(3, len(arr)):     #O(n)
        if arr[i] < min_elements[2]: #O(1) 
            min_elements[2] = arr[i] #O(1)
            insertion_sort(min_elements)  #O(1)
    
    return min_elements[0:3]


def insertion_sort(arr):
    for i in range(len(arr)): #3
        val = arr[i]
        while i > 0 and val < arr[i-1]: #
            swap(arr, i, i-1)
            i-=1

def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t

lst = [65,1,4,87,49,11,9,5,46]
print(min3(lst))
