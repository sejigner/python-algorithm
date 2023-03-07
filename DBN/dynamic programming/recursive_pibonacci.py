# 메모이제이션을 위한 리스트 초기화(0부터 100까지)
d = [0] * 101

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    
    if d[n] != 0:
        return d[n]
    d[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return d[n]

print(fibonacci(100))