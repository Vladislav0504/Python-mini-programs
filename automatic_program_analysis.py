from sys import stdin


class DisjointSets(list):

    def __init__(self, n):
        self.extend([[i + 1, 0] for i in range(n)])


    def find(self, i):
        while i != self[i - 1][0]:
            i = self[i - 1][0]
        return i


    def union(self, i, j):
        i_id, j_id = self.find(i) - 1, self.find(j) - 1
        if i_id != j_id:
            if self[i_id][1] > self[j_id][1]:
                self[j_id][0] = i_id + 1
            else:
                self[i_id][0] = j_id + 1
                if self[i_id][1] == self[j_id][1]:
                    self[j_id][1] += 1


def main():
    n, e, d = map(int, input().split())
    S = DisjointSets(n)
    res = 1
    for k, line in enumerate(stdin):
        i, j = map(int, line.split())
        if k < e:
            S.union(i, j)
        elif S.find(i) == S.find(j):
            res = 0
            break
    print(res)


if __name__ == '__main__':
    main()
