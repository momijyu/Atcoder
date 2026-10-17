n, k, t = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
now = 0
cnt = 0

for i in a:
    if i >= t:
        break
    if i > now:
        buff = i - now
        cnt += (buff + k - 1) // k
    now = max(now, i + k)
if now < t:
    buff = t - now
    cnt += (buff + k - 1) // k

print(cnt)