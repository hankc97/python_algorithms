# Given an integer array, output all the unique pairs that sum up to a specific value k.
# So the input:
# pair_sum([1,3,2,2],4)
# would return 2 pairs:
#  (1,3)
#  (2,2


def pair_sum(arr,k):
    counter = 0
    output = set()

    for num in arr:
        if num not in output:
            output.add(k - num)
        elif num in output:
            counter += 1
            output.remove(num)

    return counter

print(pair_sum([1,3,2,2],4))