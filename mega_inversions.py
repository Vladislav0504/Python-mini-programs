import math
def Merge(A, B):
  D = []
  c1 = 0
  c2 = 0
  global c
  Ai = 0
  Bi = 0
  Al = len(A)
  Bl = len(B)
  if Al > 1:
    Al -= 1
    c1 += A[Al]
  if Bl > 1:
    Bl -= 1
    c1 += B[Bl]
  while Ai < Al and Bi < Bl:
    if A[Ai][0] <= B[Bi][0]:
      D.append(A[Ai])
      if Al > 1:
        A[Al] -= A[Ai][2]
      A[Ai][1] += c2
      Ai += 1 
    else:
      c2 += 1
      D.append(B[Bi])
      c1 += Al - Ai
      c += B[Bi][1]*(Al - Ai)
      if Al > 1:
        c += A[Al]
      B[Bi][2] += Al - Ai
      Bi += 1
  if Ai == Al:
    for i in range(Bi,Bl):
      D.append(B[i])
  else:
    for i in range(Ai,Al):
      A[i][1] += c2
      D.append(A[i])
  D.append(c1)
  return D
def Mergesort(l, r, A):
  if l < r:
    m = math.floor((l + r)/2)
    return Merge(Mergesort(l, m, A), Mergesort(m + 1, r, A))
  else:
    return [A[l]]
n = int(input())
A = []
for i in range(n):
  A.append([int(input()),0,0])
c = 0 
Mergesort(0, n - 1, A)
print(c)