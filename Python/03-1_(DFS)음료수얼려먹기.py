n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
# print(graph)
# 특정한 지점의 주변 상하좌우 살펴본 뒤에 주변 지점 중 값이
# 0이면서 아직 방문하지 않은 지점 있으면 해당 지점 방문
result = 0
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 방문한 지점에서 다시 상하좌우를 살펴보면서 
        # 방문을 다시 진행하면 연결된 모든 지점을 방문할 수 있다
        # 방문하지 않은 지점수를 센다
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result) # 정답출력

