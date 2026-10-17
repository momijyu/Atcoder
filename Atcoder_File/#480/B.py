n, m = map(int, input().split())
s = []
cnt = [0] * n

for i in range(n):
    sa = input()
    s.append(sa)
#print(s)
for i in range(m):
    t = input()
    cnt2 = []
    if t in s:
        cnt[s.index(t)] += 1
        continue
    for j in range(n):
        if len(s[j]) == len(t):
            diff = 0
            for k in range(len(t)):
                if s[j][k] != t[k]:
                    diff += 1
            if diff == 1:
                cnt2.append(j)
    if len(cnt2) == 1:
        cnt[cnt2[0]] += 1

for c in cnt:
    print(c)