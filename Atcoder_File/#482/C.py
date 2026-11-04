h, w, n, q = map(int, input().split())
rc = [0] * (h + 1)
cc = [0] * (w + 1)
#めっちゃ累積和っぽい問題
for i in range(n):
    ra, ca = map(int, input().split())
    rc[ra] += 1
    cc[ca] += 1
for i in range(1, h + 1):
    rc[i] += rc[i - 1]

for i in range(1, w + 1):
    cc[i] += cc[i - 1]

for i in range(q):
    t = list(map(int, input().split()))
    if t[0] == 1:
        print(rc[t[2]] - rc[t[1] - 1])
    else:
        print(cc[t[2]] - cc[t[1] - 1])