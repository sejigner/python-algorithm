from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    # a에서 b로 이동 가능
    graph[a].append(b)
    # 진입차수 1 증가
    indegree[b] += 1


def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소에서 이동 가능한 노드들의 진입차수 1 차감
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=' ')
  
topology_sort()
    
