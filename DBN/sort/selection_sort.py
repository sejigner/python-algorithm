# 선택 정렬(Selection Sort)

arr = [6, 3, 2, 7, 1, 5, 8, 4, 10, 9]
print(arr)

for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)