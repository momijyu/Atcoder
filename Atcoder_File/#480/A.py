a = input()
b = input()
if a[0] == "A":
    if b[1] == "D":
        print("No")
        exit()
elif a[1] == "A":
    if b[0] == "D":
        print("No")
        exit()
elif b[0] == "A":
    if a[1] == "D":
        print("No")
        exit()
elif b[1] == "A":
    if a[0] == "D":
        print("No")
        exit()
print("Yes")