n = int(input())
sort_arr = []

for _ in range(n):
    name, korean, eng, math = map(str, input().split())
    sort_arr.append((name, int(korean), int(eng), int(math)))

sort_arr.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))


for x in sort_arr:
    print(x[0])