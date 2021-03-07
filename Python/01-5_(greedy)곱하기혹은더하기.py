# 왼쪽에서 오른쪽으로만 계산됨
# 0이 나오면 다음 수와 더하는 것이 당연히 큼
# 기본적으로 곱하기를 많이 해야 이득
# 조건문에 약한것 같다

num = str(input())
print(num)

result = int(num[0])
for (idx, i) in enumerate(num):
    print(idx, type(i), num[idx])
    i = int(i)
    print(num)

    # num = int(num)
    if idx < len(num) -1 and (int(num[idx+1]) == 0 or int(num[idx+1]) ==1) or (i == 0 or i == 1):
        # print('first', i)
        result += int(num[idx+1])
        # print(result)
    elif idx < len(num) -1:
        # print('second', i)
        result *= int(num[idx+1])
        # print(result)
print(result)


# solution 2
data = input()

result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 0또는 인 경우 곱하기보단 더하기
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)