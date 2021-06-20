arr = [4, 10 , 3, 11, 2]

def max_heapify(arr, current_idx, heap_size):
    parent_idx = current_idx
    left_idx = (2 * current_idx) + 1
    right_idx = (2 * current_idx) + 2

    if left_idx < heap_size and arr[left_idx] > arr[parent_idx]:
        parent_idx = left_idx
    if right_idx < heap_size and arr[right_idx] > arr[parent_idx]:
        parent_idx = right_idx
    if parent_idx != current_idx:
        arr[current_idx], arr[parent_idx] =  arr[parent_idx], arr[current_idx]
        max_heapify(arr, parent_idx, heap_size)

def heap_sort(arr):
    heap_size = len(arr) - 1

    build_heap(arr)

    for i in range(heap_size, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, 0, i)

def build_heap(arr):
    heap_size = len(arr)
    last_non_leaf_idx = heap_size // 2 - 1

    for i in range(last_non_leaf_idx, -1, -1):
        max_heapify(arr, i, heap_size)

heap_sort(arr)
print(arr)


# https://prnt.sc/163yisy