# 나의 풀이
n = int(input())
home = list(map(int, input().split()))

home.sort(reverse=True)
min_value = 987654321
result = 0

for i in range(len(home)):
    new_home = [0] * (len(home))
    print(new_home)
    for j in range(len(home)):
        new_home[j] = abs(home[j] - home[i])
    print(new_home)

    if sum(new_home) <= min_value:
        min_value = sum(new_home)
        print(min_value)
        result = home[i]

print(result) 
    
# 책의 풀이
# 핵심: 중간값에 해당하는 위치 집에 안테나 설치했을 때가 최소
n = int(input())
data = list(map(int, input().split()))
data.sort()

# n이 6이면 2
print(data[(n-1)//2])