from collections import deque

n, k = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

target_s, target_x, target_y = map(int, input().split())

# 전체 스캔하면서 큐에 추가
q = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            q.append((graph[i][j], 0, i, j))

q.sort()
q = deque(q)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    virus, s, x, y = q.popleft()

    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x-1][target_y-1])