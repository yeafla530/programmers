def find_parent(parent, x):
    if parent[x] != x:
        # x대신 parent[x]를 넣어줌
        # parent[x]의 부모 찾을때까지 재귀
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    

def union_parent(parent, a, b):
    # 이 단계에선 parent[x]값의 부모노드만 찾음
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 부모 노드만 저장되어있는것 확인
print(parent)

# 이 단계를 통해 루트 노드를 찾아저장 
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')
print()

for i in range(1, v+1):
    print(parent[i], end=' ')