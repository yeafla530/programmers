N, K = map(int, input().split())
coin = list(int(input()) for _ in range(N))
# print(coin)

d = [10001] * (K+1)

# 다이나믹 프로그래밍