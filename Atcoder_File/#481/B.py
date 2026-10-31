n, k = map(int,input().split())
a = list(map(int,input().split()))
cnt= 0
if a[0] == k:
    cnt += 1
for i in range(1,n):
    if a[i-1] != k:
        if a[i] == k:
            cnt += 1
        elif a[i-1] < k and a[i] > k:
            cnt += 1
        elif a[i-1] > k and a[i] < k:
            cnt += 1
print(cnt)