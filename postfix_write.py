from sys import stdin
class Stack(list):
    def Push(self, a):
        self.append(int(a))
    def Pop(self):
        return self.pop()
S = Stack()
for line in stdin:
    s = line.split()
    for el in s:
        if el in "+":
            S.Push(S.Pop() + S.Pop())
        elif el == "-":
            S.Push(-S.Pop() + S.Pop())
        elif el == "*":
            S.Push(S.Pop() * S.Pop())
        else:
            S.Push(el)
print(S.Pop())