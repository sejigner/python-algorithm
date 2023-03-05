arr = [5, 7, 9, 0, 3, 1, 6, 4, 8, 2]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개이면 종료
        return
    pivot = start # 첫 번째 원소를 피봇으로 지정
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]

        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

quick_sort(arr, 0, len(arr) - 1)
print(arr)