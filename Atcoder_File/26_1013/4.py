n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

ans = 0
j = len(a)
for i in range(n):
    j -= 1
    ans += a[i] * (j - i)

print(ans)