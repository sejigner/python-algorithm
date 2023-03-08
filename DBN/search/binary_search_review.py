def recursive_binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return recursive_binary_search(array, target, start, mid - 1)
    else:
        return recursive_binary_search(array, target, mid + 1, end)


arr = [4, 1, 5, 6, 8, 3, 10, 12, 14, 11, 2]
target = 8
result = recursive_binary_search(arr, target, 0, len(arr)-1)
print(result)
