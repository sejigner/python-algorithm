n = int(input())
array = []
max_value = 0

for _ in range(n):
    array.append(int(input()))

array.sort()
for i in range(n):
    max_value = max((n - i) * array[i], max_value)

print(max_value)
