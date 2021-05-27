N, M = map(int, input().split())
x, y, d = map(int, input().split()) # 1 1 0
# 2차원 리스트 입력받는 법 
game_map = [list(map(int, input().split())) for _ in range(N)]
dlist = [[0]*M for _ in range(N)] 
dlist[x][y] = 1

# print(N, M, x, y, d, game_map)
# 0-북, 1-동, 2-남, 3-서
# 0-육지, 1-바다
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
check = [False,False,False,False]
# turn_time = 0

count = 1
nx = 0
ny = 0

def turn_left():
    global d
    d -= 1
    if d == -1 : 
        d = 3

while True:
    # 북-서-남-동 / 3-2-1-0방향으로 회전
    # 1. 현재 방향 기준으로 왼쪽방향으로 회전
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    # 왼쪽 방향에 아직 가보지 않은 칸 => 회전한 후 => 이동
    if game_map[nx][ny] == 0 and dlist[nx][ny] == 0:
        dlist[nx][ny] = 1
        count += 1
        x = nx
        y = ny
        check = [False,False,False,False]
        # turn_time += 1

    # 가보지 않은칸 없으면 => 왼쪽방향으로 회전만 수행 => 1단계
    else:
        check[d] = True
        # turn_time += 1
        # continue해서 밑에 실행문이 작동을 안했던 것 


    # 네방향 모두 가본 칸이거나 바다면 바라보는 방향 유지한 채 한칸 뒤로 => 1단계
    if all(check):
    # if turn_time == 4:
        # print('hello')
        nx = x - dx[d]
        ny = y - dy[d]
        # 만약 뒤쪽이 바다여서 갈 수 없으면 종료
        # 갔던 곳이면 상관 x
        if game_map[nx][ny] == 0:
            x = nx
            y = ny
            check = [False, False, False, False]
            # turn_time = 0
        else:
            break

print(count)    

             

