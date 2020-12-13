# Median of medians
def select(arr, i):

    if len(arr)==1:
        return arr[0]

    sub_lists = [arr[i:i+5] for i in range(0, len(arr), 5)]

    for lst in sub_lists: #n/5
        insertion_sort(lst)

    
    medians = [lst[len(lst)//2] for lst in sub_lists]

    if len(medians) > 5:
        m = select(medians, len(medians)//2)
    else:
        insertion_sort(medians)
        m = medians[len(medians)//2]
    
    k = partition(arr, m)

    if i < k:
        return select(arr[0:k], i)
    elif i > k:
        return select(arr[k+1:], i-k-1)
    else:
        return m

def partition(arr, pivot):
    left = 0
    right = len(arr) - 1
    i = 0
    while i <= right:
        if arr[i] == pivot:
            i += 1
        elif arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        else:
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1
    return left

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

#Divide and conquer design
def select_min_3(arr):
    pivot = select(arr, 2)
    print(pivot)
    min_lst = [i for i in arr if i <= pivot]
    insertion_sort(min_lst)
    return min_lst  


lst = [65,1,4,87,49,11,9,5,46]
print(select_min_3(lst))
