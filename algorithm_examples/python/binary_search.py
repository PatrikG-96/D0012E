
def binary_search(arr, v):

    mid = len(arr) // 2


    if arr[mid] > v:

        return binary_search(arr[:mid], v)

    elif arr[mid] < v:

        return binary_search(arr[mid:], v)

    else:

        return mid


lst = [1,4,7,8,9,11,45]

print(binary_search(lst, 4))
