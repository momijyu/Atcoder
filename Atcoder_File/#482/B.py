s = []
mins = 6
for i in range(5):
    sa = list(input())
    s.append(sa)
for i in range(5):
    cnt = s[i].count('.')
    mins = min(mins, cnt)
for j in range(5):
    cnt = 0
    for i in range(5):
        if s[i][j] == '.':
            cnt += 1
    mins = min(mins, cnt)
cnt = 0
for i in range(5):
    if s[i][i] == '.':
        cnt += 1
mins = min(mins, cnt)
cnt = 0
for i in range(5):
    if s[i][4 - i] == '.':
        cnt += 1
mins = min(mins, cnt)

print(mins)