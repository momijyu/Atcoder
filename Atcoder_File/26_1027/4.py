x, k, d = map(int,input().split())
x = abs(x)
#残り歩数
da = x // d
# print(d)
# print(k)
if k <= da:
    print(x-k*d)
else:
    if (k - da) % 2 == 0:
        print(x % d)
    else:
        print(abs(x % d - d))