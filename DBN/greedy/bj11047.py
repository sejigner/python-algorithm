n, k = map(int, input().split())
array = []
result = 0
for _ in range(n):
    array.append(int(input()))

for num in array[::-1]:
    if num > k:
        continue
    else:
        result += k // num
        k = k % num

print(result)
