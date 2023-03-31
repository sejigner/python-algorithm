n = int(input())
array = list(map(int, input().split()))
array.sort()
result = 0

for i in range(n):
    result += array[i] * (n - i)

print(result)
