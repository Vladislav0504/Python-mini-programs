from sys import stdin


class PriorityQueue(list):

    def sift_up(self, i):
        while i > 0 and self[i] < self[(i - 1) // 2]:
            k = (i - 1) // 2
            self[i], self[k] = self[k], self[i]
            i = k
        return i


    def insert(self, x):
        self.append(x)
        self.sift_up(len(self) - 1)


    def sift_down(self, i):
        while 2 * i + 1 < len(self):
            j = 2 * i + 1
            k = j + 1
            if k < len(self) and self[j] > self[k]:
                j = k
            if self[i] <= self[j]:
                break
            self[i], self[j] = self[j], self[i]
            i = j

            
    def extract_min(self):
        if self:
            self[0], self[-1] = self[-1], self[0]
            elem = self.pop()
            self.sift_down(0)
            return elem


def main():
    n = int(input())
    P = PriorityQueue()
    for line in stdin:
        s = line.split()
        if s[0] == 'Insert':
            P.insert(-int(s[1]))
        else:
            print(-P.extract_min())


if __name__ == '__main__':
    main()
