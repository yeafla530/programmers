INF = 987654321
# 회사개수, 경로개수
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split()) # 연결된 두 회사 정보
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for i in range(1, n+1):
    graph[i][i] = 0


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)