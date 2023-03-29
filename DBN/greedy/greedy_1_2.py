# 16:50 - 16:57
n, m, k = map(int, input().split())
array = list(map(int, input().split()))
array.sort(reverse=True)
count = 0
result = 0

for _ in range(m):
    if count != k:
        result += array[0]
        count += 1
    else:
        result += array[1]
        count = 0

print(result)