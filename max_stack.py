from sys import stdin


class Stack(list):

    def push(self, a):
        if not self:
            self.append([a, 1])
        elif a <= self[-1][0]:
            self[-1][1] += 1
        else:
            self.append([a, 1])


    def delete(self):
        if self[-1][1] == 1:
            self.pop()
        else:
            self[-1][1] -= 1


    def max(self):
        return self[-1][0]


def main():
    n = input()
    S = Stack()
    for line in stdin:
        oper = line.split()
        if oper[0] == 'push':
            S.push(int(oper[1]))
        elif oper[0] == 'pop':
            S.delete()
        else:
            print(S.max())


if __name__ == '__main__':
    main()
