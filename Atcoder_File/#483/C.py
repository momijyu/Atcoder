class SegT_max:
    def __init__(self, arr):
        n = len(arr)
        # 配列サイズを2の累乗にしたい
        tmp = 1
        while tmp < n:
            tmp *= 2
        self.size = tmp
        self.tree = [(-1, 0)] * (self.size * 2)
        for i in range(n):
            self.tree[self.size + i] = arr[i]
        
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])

    def add(self, idx, val):
        if self.size < idx:return
        i = self.size + idx -1 
        self.tree[i] += val
        while i > 0:
            if i % 2 == 0:
                self.tree[i//2] = max(self.tree[i],self.tree[i+1])
            else:
                self.tree[i//2] = max(self.tree[i],self.tree[i-1])
            i //= 2

    def update(self, idx, val):
        i = self.size + idx - 1
        self.tree[i] = val
        i //= 2
        while i > 0:
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])
            i //= 2

    def get_top(self):
        return -self.tree[1][1]
#---------------------------------------------------------------------

n, m = map(int, input().split())
ac = [0] * (n + 1)
bc = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    ac[a] += 1
    bc[a].append(b)
arr = []
for i in range(1, n + 1):
    votes = ac[i]
    cand_id = -i
    arr.append((votes, cand_id))
seg = SegT_max(arr)
#print(seg.tree)
ans = []

for k in range(1, n + 1):
    seg.update(k, (-1, -k))
    for b in bc[k]:
        ac[b] += 1
        seg.update(b, (ac[b], -b))
    ans.append(seg.get_top())

    for b in bc[k]:
        ac[b] -= 1
        seg.update(b, (ac[b], -b))
    seg.update(k, (ac[k], -k))

for x in ans:
    print(x)