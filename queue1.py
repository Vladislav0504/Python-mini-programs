import sys
class Queue(list):
  def Push(self, a):
    self.append(a)
  def Pop(self):
  	print(self.pop(0))
S = Queue()
for line in sys.stdin:
  if line[0] == '+':
    if len(S) > 0:
      S.Pop()
  elif len(S) <= 4:
    S.Push(line.rstrip())