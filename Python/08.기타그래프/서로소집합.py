# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    print('a, b', a, b)
    if a < b: # b의 부모값이 더 클때
        parent[b] = a
    else: # b의 부모값이 작을때
        parent[a] = b

# 노드개수와 간선(Union연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

# 부모테이블 상에서 부모를 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# Union 연산 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 입합: ', end=' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

# print()

# 부모 테이블 내용 출력
print('부모테이블: ', end=' ')
for i in range(1, v+1):
    print(parent[i], end=' ')