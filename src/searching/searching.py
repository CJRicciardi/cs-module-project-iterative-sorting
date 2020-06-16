def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    l = len(arr)
    low = 0
    high = l - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < target:
            low = mid + 1

        elif arr[mid] > target:
            high = mid - 1

        else:
            return mid
        

    return -1  # not found
