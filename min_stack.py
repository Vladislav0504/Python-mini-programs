from sys import stdin
class Stack(list):
    def Push(self, a):
        if not self or a < self[-1][0]:
            self.append([a, 1])
        else:
            self[-1][1] += 1
    def Pop(self):
        if self[-1][1] == 1:
            self.pop()
        else:
            self[-1][1] -= 1
    def Min(self):
        return self[-1][0]
n = int(input())
S = Stack()
for line in stdin:
    oper = line.split()
    if oper[0] == '1':
        S.Push(int(oper[1]))
    elif oper[0] == '2':
  	    S.Pop()
    else:
        print(S.Min())	