from bisect import bisect_left, bisect_right
h, w, n, q = map(int, input().split())
rc = []
cc = []
for i in range(n):
    ra, ca = map(int, input().split())
    rc.append(ra)
    cc.append(ca)
#print(rc, cc)
rc.sort()
cc.sort()
for i in range(q):
    t = list(map(int, input().split()))
    if t[0] == 1:
        ans = bisect_right(rc, t[2]) - bisect_left(rc, t[1])
        print(ans)
    else:
        ans = bisect_right(cc, t[2]) - bisect_left(cc, t[1])
        print(ans)