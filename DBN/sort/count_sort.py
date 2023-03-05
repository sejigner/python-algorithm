arr = [6, 3, 2, 7, 1, 5, 8, 3, 6, 4, 10, 9]

count = [0] * (max(arr)+1)
for num in arr:
    count[num] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
        

