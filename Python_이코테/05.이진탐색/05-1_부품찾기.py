########### 이진탐색을 이용해 찾아내기 #############
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None



# N = int(input())
# array = list(map(int, input().split()))
# array.sort()
# M = int(input())
# custom = list(map(int, input().split()))


# for i in custom:
#     result = binary_search(array, i, 0, N-1)
#     if result != None:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')


######## 계수정렬을 이용해 찾아내기 ###########
# N = int(input())
# array = [0] * 1000000

# # 가게에 있는 전체 부품번호 입력 받아서 기록
# for i in input().split():
#     array[int(i)] = 1

# M = int(input())
# custom = list(map(int, input().split()))

# for i in custom:
#     if array[i] == 1:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')



######### set을 이용한 답안 ###########
N = int(input())
# 가게에 있는 전체 부품번호 입력받아 집합 자료형에 기록
array = set(map(int, input().split()))

M = int(input())
custom = list(map(int, input().split()))

for x in custom:
    if x in array:
        print('yes', end=' ')
    else:
        print('no', end=" ")