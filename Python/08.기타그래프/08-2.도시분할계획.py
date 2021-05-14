def find_city(city, x):
    if city[x] != x:
        city[x] = find_city(city, city[x])
    return city[x]


def union_city(city, a, b):
    a = find_city(city, a)
    b = find_city(city, b)
    if a < b:
        city[b] = a
    else:
        city[a] = b

n, m = map(int, input().split())
result = 0
city = [0] * (n+1)
edges = []

for i in range(1, n+1):
    city[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
last = 0

for edge in edges:
    cost, a, b = edge
    if find_city(city, a) != find_city(city, b):
        union_city(city, a, b)
        result += cost
        last = cost

print(result-last)