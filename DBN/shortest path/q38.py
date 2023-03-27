import sys
input = sys.stdin.readline
INF = int(1e9)
result = 0
n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        # 한 쪽에서라도 연결되어 있다면 비교 가능하므로
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        print(graph[i][1:])
        result += 1

print(result)


