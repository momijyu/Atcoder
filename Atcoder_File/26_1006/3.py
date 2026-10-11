n = int(input())
h = list(map(int,input().split()))
maxlen = 0
i = 0
j = 0
while True:
    if i >= n-1:
        break
    if h[i] >= h[i+1]:
        i += 1
    else:
        if maxlen < i -j:
            maxlen = i-j
        i, j = i+1, i+1
if maxlen < i -j:
    maxlen = i-j
print(maxlen)