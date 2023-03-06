n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

sorted_arr = sorted(arr, reverse=True)

for num in sorted_arr:
    print(num, end=' ')