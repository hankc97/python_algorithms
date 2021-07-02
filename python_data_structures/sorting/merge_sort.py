unsorted_array = [99,88,33,11,4,6,77]

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:len(arr)])

    return helper_merge(left, right)

def helper_merge(left, right):
    sorted_sub_array = []

    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            sorted_sub_array.append(left.pop(0))
        elif right[0] <= left[0]:
            sorted_sub_array.append(right.pop(0))
    
    return sorted_sub_array + left + right

print(merge_sort(unsorted_array))