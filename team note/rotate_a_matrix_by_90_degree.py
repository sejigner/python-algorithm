def rotate_a_matrix_by_90_degree(a):
    n = len(a)  # 행
    m = len(a)  # 열
    rotated = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            rotated[j][n - i - 1] = a[i][j]
    return rotated
