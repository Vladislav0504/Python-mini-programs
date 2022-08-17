import random
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
def KthElement(A,L,R,k):
  if L >= R:
    return A[L]
  rand = random.randint(L,R)
  A[L], A[rand] = A[rand], A[L]
  i1,i2 = Partition(L,R,A)
  if i1 - L > k:
    return KthElement(A,L,i1-1,k)
  elif k >= i1 - L and k <= i2 - L:
    return A[i2]
  else:
    return KthElement(A,i2+1,R,k-(i2-L+1))
n = int(input())
A = [int(i) for i in input().split()]
m = int(input())
for i in range(m):
  i,j,k = map(int, input().split())
  A1 = []
  for h in range(n):
    A1.append(A[h])
  print(KthElement(A1,i-1,j-1,k-1))