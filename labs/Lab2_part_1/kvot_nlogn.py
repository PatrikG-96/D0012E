
def max_quotient(arr):

    if len(arr) == 2:
        return (arr[1]/arr[0], max(arr[1], arr[0]))

    if len(arr) == 3:
        m = max(arr[1]/arr[0], arr[2]/arr[0], arr[2]/arr[1])
        M = max(arr[0], arr[1], arr[2])
        return (m,M)
        

    mid = len(arr) // 2

    (maxQL, maxL) = max_quotient(arr[0:mid])
    (maxQR, maxR) = max_quotient(arr[mid:])
    
    m = max(maxL, maxR)
    maxCross = max_cross_div(arr, mid, maxR)

    return (max(maxQL, maxQR, maxCross), m)


def max_cross_div(arr, mid, maxR):
  

    j = 0
    max_quotient = 0

    while j<=mid:

        max_quotient = max(max_quotient, maxR / arr[j])
        j += 1

    return max_quotient    

lst = [7,4,2,55,5,7,8,4,5, 70]
print(max_quotient(lst)[0])
