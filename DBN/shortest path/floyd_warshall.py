INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
# 자기 자신으로 향할 경우 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 노드 간 직접적인 이동 비용 설정
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# k번 노드를 거치는 경우와 거치지 않는 경우 비교
for k in range(1, n + 1):
    # a 행의 원소 순회
    for a in range(1, n + 1):
        # a 행 b 열 원소(기존 최단 거리)와 k번 노드를 거쳤을 때의 거리 비교
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()