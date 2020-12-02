
def bucket(arr, max_val):
    
    bucket = [0] * (max_val+1)

    for i in arr:
        bucket[i] += 1
        
    k = 0
    
    for i in range(max_val+1):

        val = bucket[i]

        for j in range(val):
            arr[k] = i
            k+=1

a = [5,4,1,2,3,1,1,2,4,1,4,1,2,4,4,1,5,6]

bucket(a, 6)

print(a)
