import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)
        # distance[now]는 모든 최단거리 정보가 저장된 배열
        # dist는 이전 노드에서 해당 노드까지의 거리
        # 비교 대상 노드가 이미 방문된 적 있다면
        if distance[now] < dist:
            continue
        # 해당 노드가 아직 방문된 적이 없다면
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])