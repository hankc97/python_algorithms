unsorted_array = [99,88,33,11,4,6,77]


def insertion_sort(arr):
    for i in range(0, len(arr)):
        j = i
        while j != 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    
    return arr

print(insertion_sort(unsorted_array))