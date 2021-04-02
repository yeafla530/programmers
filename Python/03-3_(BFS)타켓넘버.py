from collections import deque 

answer = 0
def bfs(numbers, target, idx, value):
    N = len(numbers)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    queue = deque([(0, 0)])
    print(queue)
    while queue:
        value, idx = queue.popleft()
        if idx == N:
            if value == target:
                answer += 1
        else:
            number = numbers[idx]
            queue.append((value+number, idx+1))
            queue.append((value-number, idx+1))
    return answer

        
def solution(numbers, target):
    global answer
    return bfs(numbers, target, 0, 0)