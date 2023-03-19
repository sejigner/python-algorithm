board_size = int(input())
apple = int(input())
 # 인덱스를 1부터 하기 위해 받은 사이즈보다 1 크게 맵을 설정
board = [[0] * (board_size + 1) for _ in range(board_size + 1)]
info = []  # 방향 회전 정보
for _ in range(apple):  # 2: 사과 있는 곳
        n, m = map(int, input().split())
        board[n][m] = 2

rotation_times = int(input())
for i in range(rotation_times):
    i, direction = input().split()
    info.append(int(i), direction)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1
    board[x][y] = 1  # 1: 뱀이 위치한 곳
    direction = 0
    time = 0
    index = 0  # 다음에 회전할 정보
    q = [(x, y)]  # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 벽에 부딪히지 않고, 뱀의 몸통과 부딪히지 않는다면
        if 1 <= nx and nx <= board_size and 1 <= ny and ny <= board_size and board[nx][ny] != 1:
            if board[nx][ny] == 0:  # 사과가 없다면
                board[nx][ny] = 1  # 단순 이동
                q.append((nx, ny))
                px, py = q.pop(0)  # 꼬리 제거
                board[px][py] = 0
            elif board[nx][ny] == 2:  # 사과가 있다면
                board[nx][ny] = 1
                q.append((nx, ny))
        else:  # 벽 또는 몸통과 부딪혔다면
            time += 1
            break
        x, y = nx, ny  # 다음 위치로 머리 이동
        time += 1
        if index < 1 and time == info[index][0]:  # 회전할 때면 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())
