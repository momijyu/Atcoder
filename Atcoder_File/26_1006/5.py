n, m, x = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(n)]

min_v = float('inf')

for i in range(1 << n):
    cost = 0
    s = [0] * m
    
    for j in range(n):
        if 1 & (i >> j): 
            cost += c[j][0] 
            for w in range(m):
                s[w] += c[j][1 + w]  

    if all(u >= x for u in s):
        min_v = min(min_v, cost)

if min_v == float('inf'):
    print(-1)
else:
    print(min_v)