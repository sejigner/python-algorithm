# 맵의 크기
n, m = map(int, input().split())
# 캐릭터의 처음 위치와 방향
x, y, direction = map(int, input().split())

# 리스트 컴프리헨션을 이용하여 맵 초기화
d = [[0] * m for _ in range(n)]


d[x][y] = 1  # 현재 캐릭터의 위치 방문 처리

# 전체 맵 정보(바다는 1 표시)
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
    # 북, 동, 남, 서 (일반 직교 좌표계와 x, y 방향이 다름)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 정면이 육지면서 가보지 않은 칸일 경우에 전진
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있는 경우(육지)
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
