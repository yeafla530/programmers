
N, M = map(int, input().split())
card = [list(map(int, input().split())) for _ in range(N)]

print(card)

# 행마다 제일 작은 수 구하기
# 그 중 제일 큰 수 구하기
maxData = 0
for i in range(N):
    minData = min(card[i])
    print(minData)
    if minData >= maxData:
        maxData = minData

print(maxData)

# solution 2
N, M = map(int, input().split())
result = 0

for i in range(N):
    card = [list(map(int, input().split()))]
    min_value = min(card)
    result = max(result, min_value)
