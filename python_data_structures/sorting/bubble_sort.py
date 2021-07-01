unsorted_array = [99,88,33,11,4,6,77]

def bubble_sort(arr):
    was_swapped = True
    z = len(arr) - 1

    while was_swapped:
        was_swapped = False
        for i in range(0, z):
            if arr[i] > arr[i + 1]:
                was_swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        z -= 1
    
    return arr

print(bubble_sort(unsorted_array))