N, M = map(int, input().split())
tteock = list(map(int, input().split()))
result = 0

start = 0
end = max(tteock)

while start <= end:
    total = 0 # 잘린 떡
    mid = (start + end) // 2 # 자를 중간값

    for x in tteock:
        if mid < x:
            total += x - mid
    
    # 잘린 떡양이 적으면
    if total < M:
        # 자를곳 밑으로 더 내리기
        end = mid - 1
    # 자른 떡 양이 같거나 많으면 
    else:
        # 지금 자르는 높이가 result
        result = mid
        start = mid + 1 


print(result)
