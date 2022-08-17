from sys import stdin
class Queue(list):
    def Push(self, a):
        self.append(a)
    def Pop(self):
        return self.pop(0)
m = int(input())
S = Queue()
for line in stdin:
    oper = line.split()
    if oper[0] == '+':
        S.Push(oper[1])
    else:
        print(S.Pop())	