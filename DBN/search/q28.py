def binary_search(arr, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return binary_search(arr, mid + 1, end)
    else:
        return binary_search(arr, start, mid - 1)


n = int(input())
data = list(map(int, input().split()))
result = binary_search(data, 0, n - 1)
if result == None:
    print(-1)
else:
    print(result)