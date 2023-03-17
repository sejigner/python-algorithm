n, m = map(int, input().split())
data = list(map(int,input().split()))

result = 0
for i in range(len(data) - 1):
    for j in range(i+1, len(data)):
        if data[i] != data[j]:
            result += 1
print(result)


'''
n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

for x in data:
  array[x] += 1

result = 0

for i in range(1, m + 1):
  n -= array[i]
  result += array[i] * n

print(result)
'''