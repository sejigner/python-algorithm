'''
내 풀이(순열 이용)
from itertools import permutations

def calc(num1, num2, operator):
    if operator == 0:
        return num1 + num2
    elif operator == 1:
        return num1 - num2
    elif operator == 2:
        return num1 * num2
    else:
        if num1 < 0:
            return (abs(num1) // num2) * -1
        else:
            return num1 // num2

n = int(input())
nums = list(map(int, input().split()))
data = list(map(int, input().split()))
operators = []

for i in range(len(data)):
    if data[i] != 0:
        for _ in range(data[i]):
          operators.append(i)
print(operators)
operators = list(permutations(operators, len(operators)))

result_max = -1e9
result_min = 1e9
for i in range(len(operators)):
    result = nums[0]
    for j in range(len(operators[0])):
        result = calc(result, nums[j+1], operators[i][j])
    result_max = max(result_max, result)
    result_min = min(result_min, result)

print(result_max, result_min)
'''
# DFS를 이용한 풀이
n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div

    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1

dfs(1, data[0])

print(max_value)
print(min_value)