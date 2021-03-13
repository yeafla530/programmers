# 조합 
# 순서 고려x
from itertools import combinations

N, M = map(int, input().split())
data = list(map(int, input().split()))
count = 0
result = list(combinations(data, 2))
for i in range(len(result)):
    print(result[i])
    if result[i][0] == result[i][1]:
        print(result[i][0], result[i][1])
        continue
    count += 1
print(count)

# solution 2
N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

# M은 1부터 10까지 존재 => count
ball = [0] * 11
result = 0
for i in data:
    ball[i] += 1
print(ball)
# ball 개수를 셌으니 
for i in range(1, M+1): # 1 2 3
    ball_c = 0
    for j in range(i+1, M+1): # 1 2 3
        print(j)
        ball_c += ball[j]
    print(ball[i], ball_c)
    result += ball[i] * ball_c

print(result)


# solution 3 : 책 풀이
N, M = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 n까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    n -= array[i] # 현재 공을 뺀만큼 곱해주면 됨
    result += array[i] * n