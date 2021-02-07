# solution 1
# 2중 for문 : O(n**2)
def solution(prices):
    answer = [0]*len(prices)
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j] : break
    return answer

# solution 2
# stack
def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack=[]
    for i in range(len(prices)):
    #enumerate쓸 경우 더 오래걸림
    # for i, price in enumerate(prices):
        #줄어든 주식값의 index확인
        # while stack and price < prices[stack[-1]]:
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    #stack에 남아있는 index값들
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - j - 1
    
    return answer