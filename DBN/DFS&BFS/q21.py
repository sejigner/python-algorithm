from collections import deque

n, l, r = map(int, input().split()) # L명 이상 R명 이하

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

def process(x, y, index):
    united = [] # x, y의 국가와 연결된 국가 리스트
    united.append((x, y))

    q = deque()
    q.append((x, y))
    union[x][y] = index #현재 연합의 번호 할당
    summary = graph[x][y]  # 현재 연합의 전체 인구 수
    count = 1 # 연합의 국가 수
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인접 국가 확인
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    for i, j in united:
        graph[i][j] = summary // count
    return count

total_count = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 아직 처리되지 않은 나라
                process(i, j, index)
                index += 1
    # 인덱스가 n*n이라는 것은 n*n회 process 함수가 실행되는 동안 모든 국가가 연합 조건을 충족하지 못해서 union[i][j] 값이 1에 머물러 있었다는 것을 의미한다.
    if index == n * n:
        break
    total_count += 1

print(total_count)