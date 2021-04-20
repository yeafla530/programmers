def dfs(graph, v, visited):
    # 현재노드를 방문처리
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def selection(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i] 
    print(array)

def insertion(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]: # 한칸씩 왼쪽으로 이동
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    print(array)

def quick(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면
            array[left], array[right] = array[right], array[left]
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick(array, start, right-1)
    quick(array, right+1, end)

def python_quick(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <=  pivot] # 분할된 왼쪽부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    return python_quick(left_side) + [pivot] + python_quick(right_side) 

def count_sort(array2):
    for i in range(len(array)):
        count[array[i]] += 1
    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=" ")


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array2 = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * (max(array) + 1)


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

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# dfs(graph, 1, visited)
bfs(graph, 1, visited)
# selection(array)
# insertion(array)
# quick(array, 0, len(array)-1)
print(python_quick(array))
# print(array)
count_sort(array2)