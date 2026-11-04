n = int(input())
x = list(map(int,input().split()))
print((x[-1]- x[0])/2)
for i in range(1,n-1):
    print((x[0]-x[i])/2 + (x[i]-x[-1])/2)
print((x[-1]- x[0])/2)