from collections import deque

n, m, s, t = map(int, input().split())
ab = [[] for _ in range(n + 1)]
min_v = [float("inf")] * (n + 1)
for i in range(m):
    a,b = map(int,input().split())
    ab[a].append(b)
    if b < min_v[a]:
        min_v[a] = b
#print(ab, min_v)
INF = float("inf")
costs = [INF] * (n + 1)
costs[s] = 0
q = deque([s])
while q:
    u = q.popleft()
    if u == t:
        break
    for v in ab[u]:
        cost = 0 if v == min_v[u] else 1
        if costs[v] > costs[u] + cost:
            costs[v] = costs[u] + cost
            if cost == 0:
                q.appendleft(v)
            else:
                q.append(v)
    #print(costs)
    
if costs[t] != INF:
    print(costs[t])
else:
    print(-1)