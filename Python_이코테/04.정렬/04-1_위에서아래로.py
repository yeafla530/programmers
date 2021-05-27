N = int(input())

array = [int(input()) for x in range(N)]

array.sort(reverse=True)
# print(array)

for i in range(N):
    print(array[i], end=" ")