n, m = map(int, input().split())
array = list(map(int, input().split()))
num_set = set(array)
result = 0
num = len(array)

for n in num_set:
    result += (num - array.count(n)) * array.count(n)
    num -= array.count(n)

print(result)