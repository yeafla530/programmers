N = int(input())
array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, N):
    d[i] = max(d[i-1], d[i-2] + i)

print(d[N-1])