def solution(s):
    answer = 0
    length = 1
    min_len = 987654321
    
    # if len(s) <= 2:
    #     return len(s)
    # 'a' 1인경우 주의
    while length <= len(s)//2 + 1:
        # 1개씩 자르는 경우
        result = ''
        mini_value = 1
        for x in range(0, len(s), length):
            now = s[x:x+length]
            if now == s[x+length:x+(length*2)]:
                mini_value += 1
                now = s[x+length:x+(length*2)]
            else:
                if mini_value > 1:
                    result+=str(mini_value)
                result+=now
                mini_value = 1
        # print(result)

        
        if len(result) < min_len:
            min_len = len(result)
        length += 1  
    return min_len