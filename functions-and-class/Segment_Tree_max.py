class SegT_max:
    def __init__(self,arr):
        n = len(arr)
        #配列を2累乗にしたい
        tmp = 1
        while tmp < n:tmp *= 2
        self.size = tmp
        self.tree = [0] * self.size * 2
        for i in range(1,n+1):
            self.add(i,arr[i-1])

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
    

data = [1,2,3,4,5,6,7,8]
seg = SegT_max(data)
#seg.add(1,100)
print(seg.tree)