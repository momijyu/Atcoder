n = int(input())
s = str(input())
ans = 0
cnt = 0
for i in range(n):
    if s[i] == "R":
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0
print(ans)