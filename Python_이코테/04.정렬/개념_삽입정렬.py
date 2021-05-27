array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): # 맨앞 고정
    for j in range(i, 0, -1): # idx i부터 1까지 1씩 감소하면서 반복
        if array[j] < array[j-1]: # j위치에 있는 값이 바로 앞의 값보다 작으면
            array[j], array[j-1] = array[j-1], array[j] # swap
        else: # 자기보다 작은 데이터를 만나면 고정  
            break

print(array)