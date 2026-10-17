n, w = map(int,input().split())
a, b = [], []
max_val = 0
for i in range(n):
    ai, bi = map(int,input().split())
    a.append(ai)
    b.append(bi)
for i in range(1 << n):
    c = 0
    d = 0
    for j in range(n):
        if (i >> j) & 1:
            c += b[j]
            d += a[j]
    if c <= w:
        max_val = max(max_val, d)

print(max_val)