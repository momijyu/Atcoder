n = int(input())
a = list(map(int,input().split()))

ans = float("inf")

for x in a:
    cnt = 0
    while x % 2 == 0:
        x /= 2
        cnt += 1
    if cnt < ans:
        ans = cnt

print(ans)