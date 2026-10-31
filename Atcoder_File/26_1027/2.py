m, d = map(int,input().split())
s = input()
c = [0]*m
count = 0
for i in range(m):
    if s[i] == "G":
        count = d+1
    c[i] += count
    
    if count != 0:
        count -= 1
count = 0
for i in range(m-1, -1, -1):
    if s[i] == "G":
        count = d+1
    c[i] += count
    
    if count != 0:
        count -= 1
print(c.count(0))