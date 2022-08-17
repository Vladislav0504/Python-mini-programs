from sys import stdin
class Disjoint_sets(list):
    d = {}
    def Reset(self, n):
        self.clear()
        self.d.clear()
        for i in range(n):
            self.append(i)
            self.d[i] = [i]
        return 'RESET DONE'
    def Join(self, j, k):
        if self[j] == self[k]:
            return 'ALREADY', j, k
        else:
            if len(self.d[self[j]]) > len(self.d[self[k]]):
                j, k = k, j
            d1, d2 = self[j], self[k]
            self.d[d2].extend(self.d[d1])
            for elem in self.d[d1]:
                self[elem] = self[k]
            self.d.pop(d1)
    def Check(self, j, k):
        if self[j] == self[k]:
            return 'YES'
        else:
            return 'NO'
S = Disjoint_sets()
for line in stdin:
    s = line.split()
    if s[0] == 'RESET':
        print(S.Reset(int(s[1])))
    elif s[0] == 'CHECK':
        print(S.Check(int(s[1]), int(s[2])))
    else:
        t = S.Join(int(s[1]), int(s[2]))
        if t:
            print(*t)