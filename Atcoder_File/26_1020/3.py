n = int(input())
a = []
b = []
for i in range(n):
    ai, bi = map(int,input().split())
    a.append((ai, i))
    b.append((bi, i))
#print(a, b)
a.sort() 
b.sort()
if a[0][1] != b[0][1]:
    print(max(a[0][0], b[0][0]))
else:
    print(min(a[0][0]+b[0][0], max(a[1][0], b[0][0]), max(a[0][0], b[1][0])))