n, m = map(int, input().split())
ball_list = list(map(int, input().split()))

arr = [0] * 11
result = 0
for x in ball_list:
    arr[x] += 1

for i in range(1, m+1):
    # n = b의 경우의 수
    n -= arr[i]
    result += arr[i] * n 

print(result)

