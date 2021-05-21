n = input()
lth = len(n) // 2

left_score = 0
right_score = 0

for x in range(lth):
    left_score += int(n[x])

for x in range(lth, len(n)):
    right_score += int(n[x])

if left_score == right_score:
    print('LUCKY')
else:
    print('READY')



