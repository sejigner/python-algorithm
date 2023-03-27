import heapq
INF = int(1e9)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

t = int(input())

for _ in range(t):
    n = int(input())
    distance = [[INF] * (n) for _ in range(n)]
    graph = []
    
    

    for i in range(n):
        graph.append(list(map(int, input().split())))
        

    def dijkstra():
        print(graph)
        q = [(graph[0][0], 0, 0)]
        distance[0][0] = graph[0][0]

        while q:
            dist, x, y = heapq.heappop(q)
            if distance[x][y] < dist:
                continue
            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or nx > n - 1 or 0 > ny or ny > n - 1:
                    continue
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

        print(distance[n - 1][n - 1])

    dijkstra()
