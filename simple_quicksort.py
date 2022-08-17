import random
import math
def Partition(l,r,A):
  x = A[l]
  j = l
  k = l
  for i in range(l + 1, r + 1):
    if A[i] < x:
      j += 1
      k += 1
      if i > k and k > j:
        A[j], A[i], A[k] = A[i], A[k], A[j]
      else:
        A[j], A[i] = A[i], A[j] 
    elif A[i] == x:
      k += 1
      A[k], A[i] = A[i], A[k]
  A[l], A[j] = A[j], A[l]
  return j,k
def Quicksort(l,r,A):
  while l < r:
    rand = random.randint(l,r)
    A[l], A[rand] = A[rand], A[l]
    m1,m2 = Partition(l,r,A)
    if m1 - l <= r - m2:
      if m1 > l:
        Quicksort(l,m1-1,A)
        l = m2 + 1
      else:
        l = m2 + 1
    else:
      if r > m2:
        Quicksort(m2+1,r,A)
        r = m1 - 1
      else:
        r = m1 - 1
n = int(input())
A = [int(i) for i in input().split()]
Quicksort(0,n-1,A)
for i in range(n):
  print(A[i],end=' ')