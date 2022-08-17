class Heap(list):

    def sift_up(self, i):
        k = (i - 1) // 2
        while i > 0 and (self[k][1] > self[i][1] or self[k][1] == self[i][1] and self[k][0] > self[i][0]):
            self[i], self[k] = self[k], self[i]
            i, k = k, (k - 1) // 2


    def sift_down(self, i):
        m = i
        left = 2 * i + 1
        right = left + 1
        for j in (left, right):
            if j < len(self) and (self[j][1] < self[m][1] or self[j][1] == self[m][1] and self[j][0] < self[m][0]):
                m = j
        if i != m:
            self[i], self[m] = self[m], self[i]
            self.sift_down(m)


    def insert(self, p):
        self.append(p)
        self.sift_up(len(self) - 1)


    def charge_priority(self, p):
        self[0] = p
        self.sift_down(0)


def main():
    n, m = map(int, input().split())
    t = [int(i) for i in input().split()]
    H = Heap()
    for i in range(m):
        if len(H) == 0 or len(H) < n and H[0][1] > 0:
            print(len(H), 0)
            H.insert((len(H), t[i]))
        else:
            print(H[0][0], H[0][1])
            H.charge_priority((H[0][0], H[0][1] + t[i]))


if __name__ == '__main__':
    main()
