 import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면
    if sum(food_times) <= k:
        return -1
    
    # 시간이 작은 음식부터 빼야됨 => 우선순위큐사용
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    
    length = len(food_times) # 음식 개수
    sum_value = 0 # 음식 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    # 음식을 먹기위해 사용한 시간 + (현재 가장작은 시간에서 이전시간을 뺌) * 현재 음식개수
    while sum_value + ((q[0][0] - previous) * length) <= k:
        # print(q)
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
        # print(now, sum_value, length, previous)
    
    result = sorted(q, key=lambda x: x[1]) # 음식번호 기준 정렬
    # print(result, k, sum_value)
    return result[(k-sum_value) % length][1]