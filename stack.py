from sys import stdin
class Stack(list):
    def Push(self, a):
        self.append(a)
    def Pop(self):
        return self.pop()
n = int(input())
S = Stack()
for line in stdin:
    oper = line.split()
    if oper[0] == '1':
        S.Push(oper[1])
    else:
        print(S.Pop())	