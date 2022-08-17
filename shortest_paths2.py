from sys import stdin
class Priority_queue(list):
    p = []
    def SiftUp(self, i):
        while i > 0 and self[i][0] < self[(i - 1) // 2][0]:
            self[i], self[(i - 1) // 2] = self[(i - 1) // 2], self[i]
            self.p[self[i][1]], self.p[self[(i - 1) // 2][1]] = self.p[self[(i - 1) // 2][1]], self.p[self[i][1]]
            i = (i - 1) // 2
        return i
    def Push(self, d, num):
        self.append([d, num])
        self.p.append(len(self) - 1)
        self.SiftUp(len(self) - 1)
    def SiftDown(self, i):
        while 2 * i + 1 <= len(self) - 1:
            j = 2 * i + 1
            if 2 * i + 2 <= len(self) - 1 and self[j][0] > self[2 * i + 2][0]:
                j = 2 * i + 2
            if self[i][0] <= self[j][0]:
                break
            self[i], self[j] = self[j], self[i]
            self.p[self[i][1]], self.p[self[j][1]] = self.p[self[j][1]], self.p[self[i][1]]
            i = j
    def ExtractMin(self):
        if self:
            self[0], self[-1] = self[-1], self[0]
            self.p[self[0][1]], self.p[self[-1][1]] = self.p[self[-1][1]], self.p[self[0][1]]
            elem = self.pop()
            self.p[elem[1]] = 'del'
            self.SiftDown(0)
            return elem
    def DecreaseKey(self, num, k):
        if self.p[num] != 'del':
            self[self.p[num]][0] = min(self[self.p[num]][0], k)
            self.SiftUp(self.p[num])
def Dijkstra(N, edges):
	inf = 4 * 10 ** 8
	d = [inf] * N
	d[0] = 0
	S = Priority_queue()
	for i in range(N):
		S.Push(d[i], i)
	while True:
		v = S.ExtractMin()
		if v is None or d[v[1]] == inf:
			break
		for u, w in edges[v[1]]:
			if d[v[1]] + w < d[u]:
				S.DecreaseKey(u, d[v[1]] + w)
				d[u] = d[v[1]] + w
	return d
n, m = map(int, input().split())
edges = [[] for i in range(n)]
for line in stdin:
	v, u, w = map(int, line.split())
	if v != u:
		edges[v - 1].append((u - 1, w))
		edges[u - 1].append((v - 1, w))
print(*Dijkstra(n, edges))