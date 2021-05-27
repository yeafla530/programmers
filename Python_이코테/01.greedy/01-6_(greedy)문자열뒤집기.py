# 이번엔 내가 더 효율적으로 짠 듯 ㅎ
data = input()

string = data[0]
count0 = 0
count1 = 0
for i in range(1, len(data)):
    # 0이 1로 바뀔때나 1이 0으로 바뀔때 count 
    if string == '0' and string != data[i]:
        count0 += 1
        string = data[i]
    if string == '1' and string != data[i]:
        count1 += 1
        string = data[i]
    
print(min(count0, count1))

# solution 2
data = input()
count0 = 0
count1 = 0

# 첫번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두번째 원소부터 모든 원소 확인
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] != '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))