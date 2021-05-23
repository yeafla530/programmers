# 인접 행렬
# 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식
# 연결되어있지 않은 노드끼리는 무한으로 표시

INF = 987654321

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

# 인접리스트
# 연결 리스트 자료 구조 이용해서 구현하는데 
#파이썬은 리스트 자료형이 append()와 메소드 제공하므로 
#인접리스트를 이용해 그래프 표현할 떄 단순히 2차원 리스트 사용가능
graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))
graph[2].append((0, 5))

print(graph)

# 인접행렬을 사용해야 속도가 빠름

# DFS

def dfs(graph, v, visited):
    # 시작점 방문
    visited[v] = True
    print(v, end=' ')

    # 시작점과 연결된 노드들을 하나하나 살펴본다
    for i in graph[v]:
        # 방문한 곳이 아니면 또 연결된 것들 확인하면서 재귀
        if not visited[i]:
            dfs(graph, i, visited)

# BFS
from collections import deque

def bfs(graph, start, visited):
    # 시작점을 삽입
    q = deque([start])
    # 방문 표시
    visited[start] = True

    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            # 방문한 곳이 아니면
            if not visited[i]:
                # 담고 방문처리 바로 
                q.append(i)
                visited[i] = True




graph = [
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
visited2 = [False] * 9

dfs(graph, 1, visited)
bfs(graph, 1, visited2)