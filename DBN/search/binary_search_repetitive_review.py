def repetitive_binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
        


arr = [1, 2, 4, 5, 6, 7, 8, 11, 14, 64]
target = 8
result = repetitive_binary_search(arr, target, 0, len(arr)-1)
print(result)
