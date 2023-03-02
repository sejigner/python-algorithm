n, k = map(int, input().split())
count = 0

while True:
    # 빼는 행위를 한 번에 수행
    target = (n // k) * k
    count += (n - target)
    n = target
    
    if n < k:
        break
    
    count += 1
    n //= k


# n < k 인 나머지 수에 대해 1씩 배기
count += (n - 1)
print(count)