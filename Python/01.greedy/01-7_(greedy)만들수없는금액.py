# 어려워 외워라 
N = int(input())
coin = list(map(int, input().split()))
coin.sort() # 1 1 2 3 9

target = 1
for x in coin:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

print(target)


