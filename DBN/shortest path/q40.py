import heapq
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]
distance = [(INF, i) for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

start = 1
q = []
heapq.heappush(q, (0, start))
distance[1] = (0, 1)

while q:
    dist, now = heapq.heappop(q)

    if distance[now][0] < dist:
        continue
    for i in graph[now]:
        # i[0]: 노드 인덱스 i[1]: 비용
        cost = dist + i[1]
        if cost < distance[i[0]][0]:
            distance[i[0]] = (cost, i[0])
            heapq.heappush(q, (cost, i[0]))

distance = distance[1:]
distance.sort(key= lambda x: (-x[0], x[1]))
result, index = distance[0]
count = 0
while True:
    if distance[count][0] == result:
        count += 1
        continue
    break

print(index, result, count)
