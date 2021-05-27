########## 내 풀이 ###########
# n = int(input())

# count = 1
# num = 1

# while count != n:
#     num += 1
#     if num % 2 == 0:
#         count += 1
#         continue
#     if num % 3 == 0:
#         count += 1
#         continue
#     if num % 5 == 0:
#         count += 1
#         continue
    
# print(num)

###### DP 풀이 #######
n = int(input())

ugly = [0] * n
ugly[0] = 1 # 첫번째 못생긴 수 1

# 2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0
# 처음에 곱셈값 초기화
next2, next3, next5 = 2, 3, 5

# 1부터 n까지 못생긴 수 찾기
for x in range(1, n):
    # 가능한 곱셈 결과 중에서 가장 작은 수를 선택
    ugly[x] = min(next2, next3, next5)
    # 인덱스에 따라서 곱셈 결과 증가
    if ugly[x] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[x] == next3:
        i3 += 1
        next3 = ugly[i3] * 3

    if ugly[x] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n-1])

