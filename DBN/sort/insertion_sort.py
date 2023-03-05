# 삽입 정렬(Insertion Sort)

arr = [6, 3, 2, 7, 1, 5, 8, 4, 10, 9]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        else:
            break
        
print(arr)