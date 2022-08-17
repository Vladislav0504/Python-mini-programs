class Queue(list):
  def Push(self, a):
    self.append(a)
  def Pop(self):
  	self.pop(0)
S = Queue()
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
k = 0
for i in range(len(A)):
  if B[i] == 0:
    if len(S) == 0:
      k += 1
    else:
      while len(S) > 0 and A[i] > S[-1][0]:
        S.Pop()
      if len(S) == 0:
        k += 1
  else:
    S.Push((A[i], B[i]))
print(k + len(S))