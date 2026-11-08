n,q = map(int,input().split())
k = list(map(int,input().split()))
#k.reverse()
ans = list(range(1,n+1))
for i in k:
    top = ans[:i]
    top.reverse()
    a = [-x for x in top]
    ans = a + ans[i:]
for x in ans:
    print(x)