# 위 문제처럼 모든 노선의 거리가 1이라는 조건이 있으면
# BFS사용가능

from collections import deque
def bfs(city, v, k, x, distance):
    q = deque([])
    q.append(x)
    while q:
        now = q.popleft()
        for next_node in city[now]:
            if distance[next_node] == -1:
                distance[next_node] = distance[now] + 1
                q.append(next_node)


# 도시개수, 도로개수, 최단거리정보, 출발도시번호
n, m, k, x = map(int, input().split())
city = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    city[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0
bfs(city, 1, k, x, distance)

check = False


for i in range(1, len(distance)):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)