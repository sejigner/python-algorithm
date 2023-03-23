# 중간값을 구하는 문제
n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n - 1) // 2])



