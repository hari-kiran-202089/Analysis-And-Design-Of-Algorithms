# Algorithm
'''
MERGESORT(Array)

    1. Calculate the mid value of the array
    2. Split the array into two subarrays

    3. Sort the left subarray by recursively calling mergesort functio
    4. similarly sort the right subarray

    5. Now, as two sub arrays are sorted, merge them into one array 

'''

# Implementation in Python


def mergesort(arr):

    # Base condition as this is a recursive function
    if len(arr) <= 1:
        return

    mid = len(arr)//2   # Step 1

    left = arr[:mid]    # Step 2
    right = arr[mid:]

    mergesort(left)     # Step 3
    mergesort(right)    # Step 4

    merge(arr, left, right)  # Step 5


def merge(arr, left_sub_arr, right_sub_arr):

    # We need two variable to keep track of which value we are comparing now
    i = 0
    j = 0

    # One variable to keep track where we are inserting the selected value in the original array
    k = 0

    # Keep comparing values of two sub arrays until we reach end of either of the two sub arrays
    while(i < len(left_sub_arr) and j < len(right_sub_arr)):
        if left_sub_arr[i] < right_sub_arr[j]:
            arr[k] = left_sub_arr[i]
            i += 1
        else:
            arr[k] = right_sub_arr[j]
            j += 1
        k += 1

    # After running above while loop, if still there are any values left in the left sub array then add them to original array
    while i < len(left_sub_arr):
        arr[k] = left_sub_arr[i]
        i += 1
        k += 1

    # if there are any values left in the right sub array then, add them to original array
    while j < len(right_sub_arr):
        arr[k] = right_sub_arr[j]
        j += 1
        k += 1


if __name__ == '__main__':
    array = [6, 5, 12, -10, -1, 1]
    print(f'Before Sorting: {array}')
    mergesort(array)
    print(f'After Sorting: {array}')
