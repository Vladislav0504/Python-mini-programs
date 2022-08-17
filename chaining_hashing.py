from sys import stdin


class HashTable(list):
    p, x = 1000000007, 263

    def __init__(self, m):
        self.extend([[] for i in range(m)])


    def h(self, s):
        k = 0
        for char in s[:0:-1]:
            k = (k + ord(char)) * self.x % self.p
        return (k + ord(s[0])) % self.p % len(self)


    def add(self, s):
        k = self.h(s)
        if s not in self[k]:
            self[k].append(s)


    def delete(self, s):
        try:
            self[self.h(s)].remove(s)
        except ValueError:
            return


    def find(self, s):
        if s in self[self.h(s)]:
            return 'yes'
        return 'no'


    def check(self, i):
        return self[i][::-1]


def main():
    H = HashTable(int(input())) 
    n = int(input())
    for line in stdin:
        oper, st = line.split()
        if oper == 'add':
            H.add(st)
        elif oper == 'find':
            print(H.find(st))
        elif oper == 'check':
            print(*H.check(int(st)))
        else:
            H.delete(st)


if __name__ == '__main__':
    main()
