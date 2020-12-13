
def max_quotient(arr):

    #O(1)
    if len(arr)==2:
        return (arr[1]/arr[0], min(arr[0], arr[1]), max(arr[0], arr[1]))

    if len(arr)==3:
        maxQ = max(arr[1]/arr[0], arr[2]/arr[1], arr[2]/arr[0])
        m = min(arr[0], arr[1], arr[2])
        M = max(arr[0], arr[1], arr[2])
        return (maxQ, m, M)

    middle = len(arr)//2

    (lQ, lm, lM) = max_quotient(arr[0:middle]) #T(n/2)
    (rQ, rm, rM) = max_quotient(arr[middle:]) #T(n/2)

    #O(1)
    maxQ = max(lQ, rQ, rM/lm)
    m = min(lm, rm)
    M = max(lM, rM)
    return (maxQ, m, M)

lst = [7,4,2,55,5,7,8,4,5, 70]
print(max_quotient(lst)[0])
