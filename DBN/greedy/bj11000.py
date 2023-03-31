import heapq
import sys

input = sys.stdin.readline

array = []
q = []
n = int(input())
for _ in range(n):
    start, end = map(int, input().split())
    array.append((start, end))

array.sort()
heapq.heappush(q, array[0][1])
for i in range(1, n):
    if array[i][0] < q[0]:
        heapq.heappush(q, array[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q, array[i][1])

print(len(q))
