import sys
import random

class counter:

    def __init__(self):
        self.counter = 0
    
    def reset(self):
        self.counter = 0
    
    def increment(self, val=1):
        self.counter += val

def min3(arr, count):
    min_elements = arr[0:3] #O(1)
    insertion_sort(min_elements, count) #O(1), size of min_elements is constant
    if len(arr) == 3:       #O(1)
        return min_elements
    count.increment()
    for i in range(3, len(arr)):     #O(n)
        count.increment(1)
        if arr[i] < min_elements[2]: #O(1) 
            min_elements[2] = arr[i] #O(1)
            insertion_sort(min_elements, count)  #O(1)
    
    #print(count.counter)
    return min_elements[0:3]


def insertion_sort(arr, count):
    for i in range(len(arr)): #3
        count.increment(1)
        val = arr[i]
        j = i-1
        while i > 0 and val < arr[i-1]: #
            swap(arr, i, i-1)
            count.increment(1)
            i-=1
        

        

def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t

lst = [1,2,3,4,5,6,7,8]

lst3 = [random.randint(1,1000) for i in range(10)]

#print(min3(lst))


#print(min3(lst1))

#print(min3(lst3))
##counters = 0
##count = counter()
##for i in range(1000):
##    lst1 = [random.randint(1,10) for i in range(10)]
##    c = min3(lst1, count)
##    print(len(lst1)+1, " <= ",  count.counter, " <= ", 6*(len(lst1)-2))
##    if not (len(lst1)+1 <= count.counter <= 6*(len(lst1)-2)):
##        print("shit, ", len(lst1)+1, " <= ",  count.counter, " <= ", 6*(len(lst1)-2))
##        counters += 1
##    
##    count.reset()
##print("Fails: ", counters)

count = counter()
avg = []
m = []
for i in range(10, 500+1, 10):
    sum_ = 0
    m.append(i)
    for j in range(10):
        lst = [random.randint(1,1000) for k in range(i)]
        min3(lst, count)
        sum_ += count.counter
        count.reset()
    avg.append(sum_/10)

for k in range(len(m)):
    print(avg[k])


#Base case: n=3 

#sort list, return it, done

#Induction step: assume correctness for n=p, show correctness for n=p+1

#If correct for n=p, that means that the minimum 3 elements of the subarray A[1..p] are 
#currently in the min_elements array. For element A[p+1], compare it with biggest element in 
#min_elements. If it is smaller, then replace biggest element with A[p+1] and sort min_elements. 
#Otherwise, do nothing. Min_elements now contains the minimum 3 elements of the array A[1..p+1]
