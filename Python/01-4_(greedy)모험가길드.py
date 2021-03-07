# 내가 잘못 생각함 남김없이 그룹이 이루어져야된다 생각했는데 아님
N = int(input())
horror = list(map(int, input().split()))

horror.sort(reverse=True)
# print(horror)

# [3, 2, 2, 2, 1]

# 일단 처음값 pick한 후 뒤에 pick만큼의 사람이 있는지 확인
count = 0
idx = 0
while True:
    if horror:
        pick = horror[0]
    else:
        break

    if len(horror) >= pick:
    # 있으면 pick만큼의 사람을 그룹으로 만들어 count하고  
        
        count += 1
        horror = horror[pick:]
        print('c, h', count, horror)
    else:
       break 
print(count)
# 그 뒤의 수를 체크하여 그 뒤의 수만큼 사람이 있으면 pass
# 아니면 종료한다 

# solution 2
N = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0
for i in data: # 공포도를 낮은 것부터 하나씩 확인
    print(i)
    count += 1 # 현재 그룹에 해당 모험가 포함 시키기 
    print('count', count)
    if count >= i: # 만약 인원수가 현재의 모험가 수보다 많으면
        result += 1 # 그룹에 포함시키기
        count = 0 # 초기화

print(result)
