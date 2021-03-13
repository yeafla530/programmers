# 반복문 구현
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1,n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        print('1일때 n은', n)
        return 1
        print('돌아오니', n)

    # n! = n * (n-1)를 그대로 코드로 작성하기
    print('n은', n)
    return n * factorial_recursive(n-1)
    

print('반복구현', factorial_iterative(5))
print('재귀구현', factorial_recursive(5))
