import sys

def min3(arr):

    min_elements = arr[0:3] #O(1)
    if len(arr) == 3:       #O(1)
        insertion_sort(min_elements) #O(1), size of min_elements is constant
        return min_elements

    for i in range(3, len(arr)):     #O(n)
        if arr[i] < min_elements[2]: #O(1) 
            min_elements[2] = arr[i] #O(1)
            insertion_sort(min_elements)  #O(1)

    return min_elements[0:3]


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

lst = [5,1,7,10,65,22,2]

print(min3(lst))

#Base case: n=3 

#sort list, return it, done

#Induction step: assume correctness for n=p, show correctness for n=p+1

#If correct for n=p, that means that the minimum 3 elements of the subarray A[1..p] are 
#currently in the min_elements array. For element A[p+1], compare it with biggest element in 
#min_elements. If it is smaller, then replace biggest element with A[p+1] and sort min_elements. 
#Otherwise, do nothing. Min_elements now contains the minimum 3 elements of the array A[1..p+1]