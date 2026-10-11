n, l= map(int,input().split())
s = sum(range(l, l+n))
if l >= 0:
    e = l
elif l+n -1 <= 0:
    e = l+n -1
else:
    e = 0
print(s-e)