class Queue(list):
  def Push(self, a):
    self.append(a)
  def Pop(self):
  	self.pop(0)
S = Queue()
l = [int(el) for el in input().split()]
x = 0
for el in l:
  if el == 0:
    S.Push(el)
  else:
    if len(S) > 0:
      S.Pop()
    else:
      x += 1
print(x)