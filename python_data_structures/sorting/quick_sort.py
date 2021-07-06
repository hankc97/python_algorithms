import random
unsorted_array = [99,88,33,11,4,6,77, 77]

def quick_sort(arr, left, right):
    if left == right:
        return

    i = left
    j = right

    pivot_idx = random.randint(left, right)
    pivot = arr[pivot_idx]

    while i < j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        
    if left < j:
        quick_sort(arr, left, j)
    if right > i:
        quick_sort(arr, i, right)


quick_sort(unsorted_array, 0, len(unsorted_array) - 1)
print(unsorted_array)
