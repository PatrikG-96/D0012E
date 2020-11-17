
def quicksort(arr, p, r):

    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q-1)
        quicksort(arr, q+1, r)


def partition(arr, p, r):
    x = arr[r]
    i = p-1
    for j in range(p, r):
        if arr[j] <= x:
            i=i+1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[i+1]
    arr[i+1] = arr[r]
    arr[r] = temp
    return i+1

lst = [5, 6, 7, 8, 1, 52, 5423, 67, 112, 7]
quicksort(lst, 0, len(lst)-1)
print(lst)
