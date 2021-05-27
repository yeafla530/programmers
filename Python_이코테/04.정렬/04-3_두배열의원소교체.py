N, K = map(int, input().split())
Num1 = list(map(int, input().split()))
Num2 = list(map(int, input().split()))

# 나의 풀이
# min_num = 987654321
# max_num = 0
# min_idx = 0
# max_idx = 0

# 1. K번만큼 반복
# for _ in range(K):
#     # Num1에서 작은값
#     min_num = min(Num1)
#     # Num2에서 큰값 찾기
#     max_num = max(Num2)

#     if min_num < max_num:
#         # 작은값 큰값 인덱스값을 찾아 서로 교환해주기
#         min_idx = Num1.index(min_num)
#         max_idx = Num2.index(max_num)

#         Num1[min_idx] = max_num
#         Num2[max_idx] = min_num
#     else:
#         break

# print(sum(Num1))

# 동빈나 풀이

# Num1은 오름차순 Num2는 내림차순 정렬
Num1.sort()
Num2.sort(reverse=True)

for i in range(K):
    if Num1[i] < Num2[i]:
        Num1[i], Num2[i] = Num2[i], Num1[i]
    else:
        break

print(sum(Num1))