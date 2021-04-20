N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]

def dfs(matrix, x, y):
    # print('cnt는?', cnt)
    matrix[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # print('nx, ny', nx, ny)
        if 0 <= nx < N and 0 <= ny < M:
            # print('nx, ny', nx, ny)
            if matrix[nx][ny] == 0:
                dfs(matrix, nx, ny)
    return True

result = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
           if dfs(matrix, i, j):
               result += 1

print(result)