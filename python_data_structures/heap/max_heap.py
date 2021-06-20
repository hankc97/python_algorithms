arr = [4, 10 , 3, 5 ,1]

def max_heapify(arr, current_idx, heap_size):
    parent_idx = current_idx
    left_idx = (2 * current_idx) + 1
    right_idx = (2 * current_idx) + 2

    if left_idx <= heap_size and arr[left_idx] > arr[parent_idx]:
        parent_idx = left_idx
    if right_idx <= heap_size and arr[right_idx] > arr[parent_idx]:
        parent_idx = right_idx
    if parent_idx != current_idx:
        arr[current_idx], arr[parent_idx] =  arr[parent_idx], arr[current_idx]
    
    if current_idx >= 0: 
        current_idx -= 1
        max_heapify(arr, current_idx, heap_size)

print(arr)