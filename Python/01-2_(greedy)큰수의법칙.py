# List, M, K
# 수의 list주어짐
# M 번 더함
# K만큼 겹쳐서 나오면 안됨

# N, M, K 입력받기

N, M, K = map(int, input().split())

data = list(map(int, input().split()))
data.sort() # 수 정렬

first = data[-1] # 첫번째로 큰 수
second = data[-2] # 두번째로 큰 수

print(first, second)

result = 0

count1 = (M // (K+1)) # 9 // 6 = 1
count2 =  (M % (K+1)) # 9 % 6 = 3
result += (count1 * first * K) + (count2 * first) + (count1 * second)
# 1 * 6 * 6 + 3 * 6 + 1 * 4


print(result)





# solution 2
N, M, K = map(int, input().split())

data = list(map(int, input().split()))
data.sort() # 수 정렬

first = data[-1] # 첫번째로 큰 수
second = data[-2] # 두번째로 큰 수


result = 0

# 항상 first * M + second형식이 나올 것임 
# M을 K+1번으로 나눠준 후 나머지는 first번 더해주면 됨

# 가장 큰 수가 더해지는 횟수 계산
count = int(M / (K+1)) * K # 8 / (3+1) * 3 = 2 * 3 = 6
count += M % (K+1) # 8 % (3+1) = 0

result += count * first # 6 * 큰수
result += (M - count) * second # 두번째로 큰수 더하기

print(result)

# solution 3 : 비효율적
N, M, K = map(int, input().split())

data = list(map(int, input().split()))
data.sort() # 수 정렬

first = data[-1] # 첫번째로 큰 수
second = data[-2] # 두번째로 큰 수

result = 0

while True:
    # 가장 큰 수 K번 더하기
    for i in range(K):
        if M == 0:
            break;
        result += first
        M -= 1

    if M == 0:
        break

    result += second
    m -= 1

print(result)