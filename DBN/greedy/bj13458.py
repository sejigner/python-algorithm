import sys
input = sys.stdin.readline

result = 0

n = int(input())
array = list(map(int, input().split()))
b, c = map(int, input().split())

for num in array:
    if b > num:
        result += 1
    else:
        result += 1
        num -= b
        result += num // c if num % c == 0 else (num // c) + 1

print(result)
