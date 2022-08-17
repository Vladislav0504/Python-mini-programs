class Stack(list):

    def push(self, a):
        if not self or self[-1][1] <= a:
            self.append((a, a))
        else:
            self.append((a, self[-1][1]))


    def delete(self):
        return self.pop()[0]


    def maxim(self):
        if not self:
            return 0
        return self[-1][1]


def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    m = int(input())
    S1 = Stack()
    S2 = Stack()
    for i in range(n):
        if len(S1) == m:
            for j in range(m - 1):
                S2.push(S1.delete())
            S1.delete()
        elif len(S2) > 0:
            S2.delete()
        S1.push(A[i])
        if len(S1) + len(S2) == m:
            print(max(S1.maxim(), S2.maxim()), end=' ')


if __name__ == '__main__':
    main()
