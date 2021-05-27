'''
선택정렬
1. 먼저 주어진 리스트 중에 최소값 찾는다
2. 그 값을 맨 앞에 위치한 값과 교환한다
3. 이제 맨 앞을 제외하고 다시 순회하며 최소값을 찾는다
4. 그 값을 맨 앞 위치 바로 다음 위치와 교환한다... 반복
'''
# 가장 작은 원소를 찾아서 고정되지 않은 맨앞의 원소와 교환해준다

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i] # 스와프

print(array)