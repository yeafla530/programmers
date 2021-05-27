# bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
# bisect_right(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스 반환

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x)) # 4의 왼쪽 idx
print(bisect_right(a, x)) # 4의 오른쪽 idx

# 특정 범위에 속하는 데이터 개수 구하기
def count_by_range(array, left_value, right_value):
    right_idx = bisect_right(array, right_value)
    left_idx = bisect_left(array, left_value)
    print(right_idx, left_idx)
    return right_idx - left_idx

array = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(array, 4, 4))
# 값이 [-1, 3]범위에 있는 데이터 개수 출력
print(count_by_range(array, -1, 3))