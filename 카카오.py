def solution(n, k, cmd):
    answer = ''
    del_list = []
    friends = [i for i in range(n)]
    now_k = k # 현재의 idx?
    now_v = friends[now_k] # 현재 value
    # "U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
    # "D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
    # "C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
    # "Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
    for md in cmd:
        if len(md) > 2:
            action = md.split(' ')[0]
            if action == 'D':
                now_k += int(md.split(' ')[1])
                print('D수행', now_k, now_v)
            if action == 'U':
                now_k -= int(md.split(' ')[1])
                print('U수행', now_k, now_v)
                
        else:
            action = md
            if action == 'C':
                del_list.append(now_k)
                friends.remove(now_k)
                if now_k > len(friends) -1:
                    now_k = len(friends) - 1
                elif now_k < 0:
                    now_k= 0
                else:
                    now_k = now_k + 1
                now_v = friends[now_k]
                print('C알때', now_k, now_v, friends)

            if action == 'Z':
                now_v = friends[now_k]
                input_v = del_list.pop()
                friends.insert(input_v, input_v) 
                print('nowv',now_v)
                now_k = friends.index(now_v)
                print('z시', now_k)
    for i in range(n):
        if i in friends:
            answer += 'O'
        else:
            answer += 'X'
    print(answer)


solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])