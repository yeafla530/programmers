# 시각
# N입력되면 N시 59분 59초까지 시각중 3 하나라도 포함되는 모든 경우 구하라

N = int(input())

count = 0
for i in range(N+1):
    for j in range(60):
        for z in range(60):
            # if '3' in str(i) or '3' in str(j) or '3' in str(z):
            if '3' in str(i) + str(j) + str(z):
                count += 1
     

print(count)