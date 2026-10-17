n, q = map(int, input().split())
l = [0, 0] + list(map(int, input().split()))
r = [0] + list(map(int, input().split()))

# r の前から min さん
rm = r.copy()
m = rm[1]
for i in range(1, n):
    if rm[i] < m:
        m = rm[i]
    else:
        rm[i] = m

# l の後ろから min さん
lm = l.copy()
m = lm[n]
for i in range(n, 1, -1):
    if lm[i] < m:
        m = lm[i]
    else:
        lm[i] = m
#print(rm, lm)
for _ in range(q):
    s, t = map(int, input().split())
    if s < t:
        ans = r[s]
        if s > 1:
            ans = min(ans, l[s] + rm[s - 1])
        print(ans)
    else:
        ans = l[s]
        if s < n:
            ans = min(ans, r[s] + lm[s + 1])
        print(ans)