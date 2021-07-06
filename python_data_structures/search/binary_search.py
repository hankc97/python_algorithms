unsorted_array = [99,88,33,11,4,6,77, 77]

sorted_arr = sorted(unsorted_array)

def binary_search(arr, left, right, target):
    mid = (left + right) // 2

    if target == arr[mid]:
        return True
    if len(arr[left:right]) < 2:
        return None

    if arr[mid] > target:
        return binary_search(arr, left, mid - 1, target)
    elif arr[mid] < target:
        return binary_search(arr, mid + 1, right, target)

print(binary_search(sorted_arr, 0, len(sorted_arr) - 1, 77))
