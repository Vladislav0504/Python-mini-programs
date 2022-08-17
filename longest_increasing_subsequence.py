def LIS(n,A):
  D = [-10**9-1]
  prev = [-1] * n
  Ind = [0] * n
  for j in range(1,n + 1):
    D.append(10**9+1)
  k = 0
  ind = 0
  for j in range(n):
    l, r = 0, n
    while l <= r:
      m = (l + r) // 2
      if D[m] < A[j]:
        l = m + 1
      else:
        r = m - 1
    if A[j] < D[r + 1]:
      D[r + 1] = A[j]
      Ind[r] = j
      if j > 0 and r > 0:
        prev[j] = Ind[r - 1]
    if r + 1 > k:
      k = r + 1
      ind = j
  print(k)
  B = [A[ind]]
  while prev[ind] != -1:
    ind = prev[ind]
    B.append(A[ind])
  return B[::-1]
n = int(input())
A = [int(i) for i in input().split()]
L = LIS(n,A)
for elem in L:
  print(elem,end=' ')