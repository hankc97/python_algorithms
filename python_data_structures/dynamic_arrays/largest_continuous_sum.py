from pdb import set_trace as bp
# Given an array of integers (positive and negative) find the largest continuous sum.

def large_cont_sum(arr): 
    cont_sum = arr[0]
    largest_sum = arr[0]

    if len(arr) == 0:
        return 0

    for i in range(0, len(arr) - 1):
        cont_sum = (cont_sum + arr[i+1])
        
        if cont_sum <= 0:
            cont_sum = arr[i+1]
        if largest_sum < cont_sum:
            largest_sum = cont_sum

    return largest_sum


print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1])) #29
