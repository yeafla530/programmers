def solution(left, right):
    answer = 0
    
    for num in range(left, right+1):
        count = 0
        for i in range(1, num+1):
            if num % i == 0:
                # print(num, i)
                count += 1
        # print(count)
        if count % 2 == 0:
            answer += num
        else:
            answer -= num
        
        
    return answer