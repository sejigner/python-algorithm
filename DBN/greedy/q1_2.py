# 17:32 - 17:47
n = int(input())
array = list(map(int, input().split()))
array.sort()
count = 0
result = 0

for value in array:
    count += 1
    if count >= value:
        result += 1
        count = 0

print(result)