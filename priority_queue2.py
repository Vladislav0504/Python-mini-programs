from sys import stdin
class Priority_queue(list):
    p = []
    def SiftUp(self, i):
        while i > 0 and self[i][0] < self[(i - 1) // 2][0]:
            self[i], self[(i - 1) // 2] = self[(i - 1) // 2], self[i]
            self.p[self[i][1]], self.p[self[(i - 1) // 2][1]] = self.p[self[(i - 1) // 2][1]], self.p[self[i][1]]
            i = (i - 1) // 2
        return i
    def Push(self, x, num):
        self.append([x, num])
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
        self.p.append('n')
        if not self:
            return ['*']
        self[0], self[-1] = self[-1], self[0]
        self.p[self[0][1]], self.p[self[-1][1]] = self.p[self[-1][1]], self.p[self[0][1]]
        elem = self.pop()
        self.p[elem[1]] = 'del'
        self.SiftDown(0)
        return elem[0], elem[1] + 1
    def DecreaseKey(self, num, k):
        self.p.append('n')
        if self.p[num] != 'del':
            self[self.p[num]][0] = min(self[self.p[num]][0], k)
            self.SiftUp(self.p[num])
S = Priority_queue()
for i, line in enumerate(stdin):
    s = line.split()
    if s[0] == 'push':
        S.Push(int(s[1]), i)
    elif s[0] == 'extract-min':
        print(*S.ExtractMin())
    else:
        S.DecreaseKey(int(s[1]) - 1, int(s[2]))