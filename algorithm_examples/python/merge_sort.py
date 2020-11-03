
def merge_sort(arr):
    if len(arr) > 1:

        #Split array in the middle
        middle = len(arr)//2
        left = arr[:middle]
        right = arr [middle:]

        #Recursive merge_sort call for both halves
        merge_sort(left)
        merge_sort(right)

        #merge the two halves with arr
        merge(arr, left, right)


def merge(arr, left, right):

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i+=1
            k+=1
        else:
            arr[k] = right[j]
            j+=1
            k+=1

    #If either right or left array hasn't been fully iterated through
    #do it here
    while i < len(left):
        arr[k] = left[i]
        i+=1
        k+=1

    while j < len(right):
        arr[k] = right[j]
        j+=1
        k+=1


lst = [51,14,66,1,2,9,0,11]
merge_sort(lst)
print(lst)
