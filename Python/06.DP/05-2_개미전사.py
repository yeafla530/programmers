n = int(input())
array = list(map(int, input().split()))

# 보텀업 방식
d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
# 최적값 찾기
for i in range(2, n):
    # 계속 반복하여 최대값 저장 후 비교
    d[i] = max(d[i-1], d[i-2] + array[i])

# 출력
print(d[n-1])