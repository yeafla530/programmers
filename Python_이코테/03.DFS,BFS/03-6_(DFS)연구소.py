n, m = map(int, input().split())
mapping = []
formatting = [[0]*m for _ in range(n)]
for _ in range(n):
    mapping.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = 0

# DFS를 이용해 각 바이러스 사방으로 퍼지게 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny) 

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global result
    # 울타리 3개까지만 가능
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = mapping[i][j]
        # 각 바이러스 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, get_score())
        return 
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if mapping[i][j] == 0:
                mapping[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)