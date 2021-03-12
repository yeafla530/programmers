N, M = map(int, input().split())
x, y, d = map(int, input().split()) # 1 1 0
# 2차원 리스트 입력받는 법 
game_map = [list(map(int, input().split())) for _ in range(N)]

# print(N, M, x, y, d, game_map)
# 0-북, 1-동, 2-남, 3-서
# 0-육지, 1-바다
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
check = [False,False,False,False]
check2 = [True]

count = 0
flag = True


nx = 0
ny = 0
while flag:
    # 북-서-남-동 / 3-2-1-0방향으로 회전
    # 1. 현재 방향 기준으로 왼쪽방향으로 회전
    d = d - 1
    if d < 0: 
        d = 4 + d
    nx = x + dx[d]
    ny = y + dy[d]

    # 왼쪽 방향에 아직 가보지 않은 칸 => 회전한 후 => 이동
    if 0<=nx<N and 0<=ny<M and game_map[nx][ny] == 0:
        game_map[nx][ny] = 1
        count += 1
        x = nx
        y = ny
        d = d - 1
        if d < 0: 
            d = 4 + d
        continue

    # 가보지 않은칸 없으면 => 왼쪽방향으로 회전만 수행 => 1단계
    elif 0<=nx<N and 0<=ny<M and game_map[nx][ny] == 1:
        d = d - 1
        if d < 0: 
            d = 4 + d
        check[d] = True
        continue

    # 네방향 모두 가본 칸이거나 바다면 바라보는 방향 유지한 채 한칸 뒤로 => 1단계
    if all(check):
        nx = x + dx[d]*(-1)
        ny = y + dy[d]*(-1)
        # 만약 뒤쪽이 바다여서 갈 수 없으면 종료
        if 0<=nx<N and 0<=ny<M and game_map[nx][ny] == 0:
            count += 1
            check = [False, False, False, False]
        else:
            flag = False
            break

print(check)    

             

