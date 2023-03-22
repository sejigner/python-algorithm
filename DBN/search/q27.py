import bisect

n, x = map(int, input().split())
data = list(map(int, input().split()))

left, right = bisect.bisect_left(data, n), bisect.bisect_right(data, n)
result = right - left

if result == 0:
    print(-1)
else:
    print(result)
