
def insertion_sort(arr):

    i = 1
    
    while i < len(arr):
        j = i -1 
        x = arr[i]
        while j >= 0 and arr[j] > x:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = x
        i+=1

            
lst = [1,65,34,2,77,0,7,1,54]
insertion_sort(lst)
print(lst)
    
