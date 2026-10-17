from collections import deque
s = input()
q = int(input())
ir = False
d = deque(s)
for i in range(q):
    a = list(input().split())
    if a[0] == "1":
        #print(1111111)
        ir = not ir
    else:
        if a[1] == "1" and not ir:
            d.appendleft(a[2])
        elif a[1] == "2" and ir:
            d.appendleft(a[2])
        else:
            d.append(a[2])

if ir:
    d.reverse()
print("".join(d))