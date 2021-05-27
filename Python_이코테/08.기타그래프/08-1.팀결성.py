def find_team(team, x):
    if team[x] != x:
        team[x] = find_team(team, team[x])
    return team[x]

def union_team(team, a, b):
    a = find_team(team, a)
    b = find_team(team, b)
    if a < b:
        team[b] = a
    else:
        team[a] = b

n, m = map(int, input().split())
team = [0] * (n+1)
result = []

for i in range(1, n+1):
    team[i] = i

for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:  
        union_team(team, a, b)
    if c == 1:
        if find_team(team, a) == find_team(team, b):
            result.append("YES")
        else:
            result.append("NO")

for re in result:
    print(re)