
def binary_search2(arr, start, end, value):

    mid = (end + start) // 2

    if arr[mid] > value:

        return binary_search2(arr, start, mid, value)

    elif arr[mid] < value:

        return binary_search2(arr, mid+1, end, value)

    return mid

lst = [1,4,7,8,9,11,45]

print(binary_search2(lst, 0, len(lst), 45))
