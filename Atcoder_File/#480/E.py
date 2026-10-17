a, b = int,input().split()
c, d = int,input().split()
if a == "A":
    if d == "D":
        print("No")
        exit()
elif b == "A":
    if c == "D":
        print("No")
        exit()
elif c == "A":
    if b == "D":
        print("No")
        exit()
elif d == "A":
    if a == "D":
        print("No")
        exit()
print("Yes")