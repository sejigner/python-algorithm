# 17:03 - 17:10
max_value = 0

n, m = map(int, input().split())
for _ in range(n):
    array = list(map(int, input().split()))
    max_value = max(max_value, min(array))

print(max_value)