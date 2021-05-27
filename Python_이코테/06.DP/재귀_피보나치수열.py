# 재귀 => O(2^n)으로 매우 비효율적
# f(6) f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(2) f(1) f(4) f(3) f(2) f(1) f(2) 8
def fibo(x):
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)


print(fibo(6))



