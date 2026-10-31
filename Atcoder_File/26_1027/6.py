from collections import Counter
t = int(input())
for i in range(t):
    s = list(input())
    #print(s)
    c = Counter(s)
    #print(list(c.values())[0])
    if list(c.values())[0] > (len(s)+1)//2:
        print("Yes")
    else:
        print("No")