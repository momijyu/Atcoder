q = int(input())
id = 1
name = {}

for i in range(q):
    s = str(input())
    if s in name:
        print(name[s])
    else:
        name[s] = id
        print(name[s])
        id += 1