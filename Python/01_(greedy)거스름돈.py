n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += n // coin # 몫구하기
    print('count',count)
    n %= coin # 나머지 구하기
    print('n', n)
print('answer', count)

