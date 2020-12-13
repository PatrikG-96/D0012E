import sys

def maxp_dac(arr):

    if len(arr) == 2:
        return arr[0]*arr[1]

    if len(arr) == 3:
        return max(arr[0]*arr[1], arr[2]*arr[1], arr[0]*arr[1]*arr[2])

    mid = len(arr)//2
    
    left_max = maxp_dac(arr[0:mid])
    right_max = maxp_dac(arr[mid:])

    cross_max = cross_mult(arr, mid)

    return max(left_max, right_max, cross_max)


def cross_mult(arr, mid):

    print("Cross mult for arr: ", arr, " with mid as ", mid)
    p = 1
    right_max = left_max = -sys.maxsize
    right_min = left_min = sys.maxsize
    for i in range(mid-1, 0-1, -1):
        p = p * arr[i]
        right_max = max(right_max, p)
        right_min = min(right_min, p)

    p = 1
    for j in range(mid, len(arr)):
        p = p * arr[j]
        left_max = max(left_max, p)
        left_min = min(left_min, p)

    return max(right_max * left_max, left_min*right_min)
    
def maxp_incr(arr, p):

    if len(arr) == 0:
        return p

    return maxp2(arr[1:], arr[0]*p)

lst = [2,5,10,-2,7, -1, 2, 1, -5]
print(maxp_dac(lst))
lst = [1,2,3,4]
print(maxp_incr(lst, 1))
print(maxp_dac(lst))
