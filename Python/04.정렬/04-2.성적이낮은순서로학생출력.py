N = int(input())

# array = [tuple(input().split()) for _ in range(N)]
# print(array)
array = []
for i in range(N):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student: int(student[1]))

for student in array:
    print(student[0], end=' ')