q = int(input())
s = input()
t = input()

tg = [0] * (len(s) + 1)
for i in range(len(s) - len(t) + 1):
    if s[i : i + len(t)] == t:
        tg[i + 1] = 1

#print(tg)
for i in range(len(s)):
    tg[i + 1] += tg[i]

for i in range(q):
    l, r = map(int, input().split())
    if r - l + 1 < len(t):
        print("No")
    elif tg[r - len(t) + 1] - tg[l - 1] > 0:
        print("Yes")
    else:
        print("No")