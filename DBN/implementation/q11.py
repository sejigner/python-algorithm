def solution():
    board_size = int(input())
    board = [[0] * board_size for _ in range(board_size)]
    apple = int(input())
    for i in range(apple):
        n, m = map(int, input().split())
        board[n][m] = 2
    rotation_times = int(input())
    movement = [0] * 101
    second = 0

    for i in range(rotation_times):
        i, direction = input().split()
        movement[int(i)] = direction

    for i in range(board_size):
        board[0][i] = 1
        board[board_size-1][i] = 1
        board[i][0] = 1
        board[i][board_size-1] = 1

    board[1][1] = 1
    x, y = 1, 1  # x행, y열
    direction = 1  # 동0 남1 서2 북3
    for i in range(board_size):
        for j in range(board_size):
            print(board[i][j], end= ' ')
        print()
    while True:
        second += 1
        if movement[second] == 0:
            if direction == 0:
                if board[x][y + 1] == 1:
                    return second
                elif board[x][y + 1] == 2:
                    board[x][y] = 1
                    board[x][y + 1] = 1
                else:
                    board[x][y] = 0
                    board[x][y + 1] = 1
                y += 1
            if direction == 1:
                if board[x + 1][y] == 1:
                    return second
                elif board[x + 1][y] == 2:
                    board[x][y] = 1
                    board[x + 1][y] = 1
                else:
                    board[x][y] = 0
                    board[x + 1][y] = 1
                x += 1
            if direction == 2:
                if board[x][y - 1] == 1:
                    return second
                elif board[x][y - 1] == 2:
                    board[x][y] = 1
                    board[x][y - 1] = 1
                else:
                    board[x][y] = 0
                    board[x][y - 1] = 1
                y -= 1
            else:
                if board[x - 1][y] == 1:
                    return second
                elif board[x - 1][y] == 2:
                    board[x][y] = 1
                    board[x - 1][y] = 1
                else:
                    board[x][y] = 0
                    board[x - 1][y] = 1
                x -= 1

        elif movement[second] == 'L':
            direction = (direction + 1) % 4

        else:
            direction = (direction + 3) % 4


print(solution())
