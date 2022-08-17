from sys import stdin


class DisjointSets(list):

    def __init__(self, n, r):
        self.extend([[i + 1, 0, r[i]] for i in range(n)])


    def find(self, i):
        while i != self[i - 1][0]:
            i = self[i - 1][0]
        return i


    def union(self, i, j):
        i_id, j_id = self.find(i) - 1, self.find(j) - 1
        if i_id != j_id:
            if self[i_id][1] > self[j_id][1]:
                self[j_id][0] = i_id + 1
                self[i_id][2] += self[j_id][2]
            else:
                self[i_id][0] = j_id + 1
                self[j_id][2] += self[i_id][2]
                if self[i_id][1] == self[j_id][1]:
                    self[j_id][1] += 1


def main():
    n, m = map(int, input().split())
    r = [int(i) for i in input().split()]
    S = DisjointSets(n, r)
    M = max(r)
    for line in stdin:
        dest, source = map(int, line.split())
        S.union(dest, source)
        M = max(M, S[S.find(dest) - 1][2])
        print(M)


if __name__ == '__main__':
    main()
