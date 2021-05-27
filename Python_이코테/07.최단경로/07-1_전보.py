import heapq

# 도시개수, 통로개수, 메세지보내고자 하는 도시 C
n, m, start = map(int, input().split())
INF = 987654321
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    # 특정도시 a,에서 b로 이어지는 통로가 있으며 메세지 전달되는 시간이 z
    a, b, z = map(int, input().split())
    graph[a].append((b, z)) # (도시, 시간) 

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: 
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 도달할 수 있는 노드 개수
count = 0
# 도달할 수 있는 노드 중에서 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    # 도달할 수 있는 노드인 겨우
    if d != INF:
        count +=1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count-1
print(count-1, max_distance)