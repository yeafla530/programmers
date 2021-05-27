N, K = map(int, input().split())
coin = list(int(input()) for _ in range(N))
# print(coin)

d = [10001] * (K+1)

# 다이나믹 프로그래밍 진행(보텀업)
d[0] = 0
# 코인 종류 추출
for c in coin:
    # 코인의 최소값 ~ K값까지
    for j in range(c, K+1):
        # 처음에 d[0] 0
        if d[j - c] != 10001:
            d[j] = min(d[j], d[j-c] + 1)

# 계산된 결과 출력
if d[K] == 10001:
    print(-1)
else:
    print(d[K])   
