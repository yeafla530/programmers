# 최적 부분구조 + 중복되는 부분문제

N = int(input())
d = [0] * (N+2)

for i in range(2, N+1):
    # 현재 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 현재 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
        print(d[i])

    # 현재 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
        print(d[i])

    # 현재 수가 5로 나누어 지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
        print(d[i])

    print(d)

print(d[N])
