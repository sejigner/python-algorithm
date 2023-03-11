import sys
input = sys.stdin.readline
INF = int(1e9)
# 노드의 개수, 간선의 개수 
n, m = map(int, input().split())
# 시작 노드
start = int(input())

# n + 1 개의 그래프 초기화(인덱스 0부터 n까지 n + 1개)
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    # a 노드에서 b 노드로 가는 비용이 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        # 해당 인덱스의 노드와 시작 노드 간 가장 적은 비용을 가진 노드의 인덱스 반환
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    # 시작 노드와 연결된 노드 탐색
    for j in graph[start]:
        # 시작 노드와 연결된 노드의 2번째 요소(비용)을 해당 노드까지의 거리를 저장하는 리스트에 업데이트
        distance[j[0]] = j[1]
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            # now 노드와 연결된 노드의 비용과 다른 경로를 이용했을 때의 비용을 비교하여 더 작은 값으로 업데이트
            cost = distance[now] + j[1] # 시작 노드부터 현 노드까지의 비용 + 현 노드와 다른 노드 간 비용
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])