N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]

d = [987654321] * (K+1)
d[0] = 0 

for c in coin:
    for j in range(c, K+1):
        if d[j-c] != 987654321:
            d[j] = min(d[j], d[j-c] + 1)

if d[K] == 987654321:
    print(-1)
else:
    print(d[K])


