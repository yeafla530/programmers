# 수평 2 수직 1
# 수직 2 수평 1

Loc = input() # 위치
N = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x = int(N.index(Loc[0])) + 1
y = int(Loc[1])
print(x, y)

dx = [-2, -2, 2, 2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

count = 0

# dx길이만큼 시행
for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    else:
        count += 1

print(count)


# solution 2
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]) - ord('a')) + 1
result = 0

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [
    (-2, -1), (-1, -2), (1, -2), (2, -1),
    (2, 1), (1, 2), (-1, 2), (-2, 1)
]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1 

print(result)







