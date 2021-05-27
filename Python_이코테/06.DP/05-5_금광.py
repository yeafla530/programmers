for tc in range(int(input())):
    # 금광 정보
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m
    print(dp)
    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # n=0인경우
            if i == 0: left_up = 0
            else:
                left_up = dp[i-1][j-1]
            if i == n-1: left_down = 0
            else:
                left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    
    print(result)