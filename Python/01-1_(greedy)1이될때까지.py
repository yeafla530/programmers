# 내 풀이
# n, k = map(int, input().split())
# count = 0
# while n != 1:
#     if n % k == 0:
#         n //= k
#         count += 1
#         print('작아?',n)
#     else :
#         n -= 1
#         print('큰상황',n)
#         count += 1


# print(count)

# solution 1
# N이 K보다 클때와 아닐때로 나누기

n, k = map(int, input().split())
count = 0

while n >= k:
   while n % k != 0:
       n -= 1
       count += 1
    n //= k
    count += 1

while n > 1:
    n -= 1
    count += 1



print(count)

# solution 2
# N, K를 공백으로 구분하여 입력하기 
n, k = map(int, input(),split())
result = 0

while True:
    # (N == K로 나누어 떨어지는 수)가 될때까지 1씩 빼기
    target = 









