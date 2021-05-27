string = input()

alpha_arr = []
num_sum = 0

for i in range(len(string)):
    if string[i].isalpha():
        alpha_arr.append(string[i])
    else:
        num_sum += int(string[i])

alpha_arr.sort()

result = ''
result = ''.join(alpha_arr)
print(result+str(num_sum))