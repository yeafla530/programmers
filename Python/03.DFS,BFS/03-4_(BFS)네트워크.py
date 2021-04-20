from collections import deque

def bfs(n, computers, com, visited):
    queue = deque([com])
    while queue:
        com = queue.popleft()
        visited[com] = True
        for connect in range(n):
            if connect != com and computers[com][connect] and visited[connect] == False:
                queue.append(connect)
    

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for com in range(n):
        if visited[com] == False:
            bfs(n, computers, com, visited)
            answer += 1
    return answer