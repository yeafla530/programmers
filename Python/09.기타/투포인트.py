n = 5 # 데이터 개수
m = 5 # 찾고자 하는 값
data = [1, 2, 3, 2, 5]

count = 0 # m인경우 몇갠지
i_sum = 0
end = 0
for start in range(n):
    while end < n and i_sum < m:
        i_sum = data[end]
        end += 1
    
    if i_sum == m:
        count += 1
    i_sum -= data[start]
print(count)