N = int(input())
plans = input().split()
# print(direction) # ['R', 'R', 'L', 'R', 'R'] list로 담김

x, y = 1, 1
# L, R, U, D에 따른 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

# 이동 계획 하나씩 확인
for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > N or ny < 1 or ny > N:
        continue
    x, y = nx, ny

print(x, y) 


