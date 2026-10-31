from heapq import *
q, v = map(int,input().split())
heap = []
for i in range(q):
    a = list(input().split())
    if a[0] == "1":
        a1 = int(a[1])
        a2 = int(a[2])
        heappush(heap, -(a2-a1))
    else:
        if len(heap) == 0:
            print(-1)
        else:
            #print(heap)
            print(min(-heappop(heap) + int(a[1]),v))