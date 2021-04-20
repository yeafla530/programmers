# 재귀구현
# def binaray_search(array, target, start, end):
#     # target값이 없는 경우
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     # 찾은 경우 중간점 인덱스 반환
#     if array[mid] == target:
#         # mid idx반환
#         return mid
#     elif array[mid] > target: # 중간값이 target값보다 큰 경우(target의 오른쪽)
#         # 중간값의 왼쪽 확인
#         return binaray_search(array, target, start, mid-1)
#     else: # 중간값이 target보다 작은 경우
#         # 중간값의 오른쪽 확인
#         return binaray_search(array, target, mid+1, end)

# 반복문 구현
def binaray_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None



n, target = map(int, input().split())
array = list(map(int, input().split()))

# print(n, target, array)

# 이진탐색 수행 결과 출력
result = binaray_search(array, target, 0, n-1)
if result == None:
    print('원소 존재 안함')
else:
    print(result + 1) # 몇번째에 존재하는지 반환