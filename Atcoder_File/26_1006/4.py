s = input()

ans = 0
for i in range(10000):
    num = str(i).zfill(4)
    
    c = True
    for d in range(10):
        if s[d] == 'o':
            if str(d) not in num:
                c = False
                break
        if s[d] == 'x':
            if str(d) in num:
                c = False
                break
    if c:
        ans += 1

print(ans)