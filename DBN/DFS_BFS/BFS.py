from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 데크 라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소 삭제하고 반환
        v = queue.popleft()
        print(v, end=' ')
        # 해당 노드와 인접하고 아직 방문되지 않은 노드의 원소를 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    # 1번 노드부터 시작
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)