from sys import stdin
class priority_queue(list):
    p = []
    def sift_up(self, i):
        while i > 0 and self[i][0] < self[(i - 1) // 2][0]:
            self[i], self[(i - 1) // 2] = self[(i - 1) // 2], self[i]
            self.p[self[i][1]], self.p[self[(i - 1) // 2][1]] = self.p[self[(i - 1) // 2][1]], self.p[self[i][1]]
            i = (i - 1) // 2
        return i
    def push(self, d, num):
        self.append([d, num])
        self.p.append(len(self) - 1)
        self.sift_up(len(self) - 1)
    def sift_down(self, i):
        while 2 * i + 1 <= len(self) - 1:
            j = 2 * i + 1
            if 2 * i + 2 <= len(self) - 1 and self[j][0] > self[2 * i + 2][0]:
                j = 2 * i + 2
            if self[i][0] <= self[j][0]:
                break
            self[i], self[j] = self[j], self[i]
            self.p[self[i][1]], self.p[self[j][1]] = self.p[self[j][1]], self.p[self[i][1]]
            i = j
    def extract_min(self):
        if self:
            self[0], self[-1] = self[-1], self[0]
            self.p[self[0][1]], self.p[self[-1][1]] = self.p[self[-1][1]], self.p[self[0][1]]
            elem = self.pop()
            self.p[elem[1]] = 'del'
            self.sift_down(0)
            return elem
    def decrease_key(self, num, k):
        if self.p[num] != 'del':
            self[self.p[num]][0] = min(self[self.p[num]][0], k)
            self.sift_up(self.p[num])
def prim(N, edges):
    inf = 2 * 10 ** 5
    d = [inf] * N
    d[0] = 0
    r = 0
    S = priority_queue()
    for i in range(N):
        S.push(d[i], i)
    while True:
        v = S.extract_min()
        if v is None or d[v[1]] == inf:
            break
        r += d[v[1]]
        for u, w in edges[v[1]]:
            if w < d[u]:
                S.decrease_key(u, w)
                d[u] = w
    return r
n, m = map(int, input().split())
edges = [[] for i in range(n)]
for line in stdin:
	v, u, w = map(int, line.split())
	if v != u:
		edges[v - 1].append((u - 1, w))
		edges[u - 1].append((v - 1, w))
print(prim(n, edges))