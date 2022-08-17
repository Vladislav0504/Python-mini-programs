n = int(input())
P = [int(i) for i in input().split()]
k =int(input())
A = []
B = []
for i in range(k):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)
P.sort()
for j in range(k):
  c = 0
  l, r = 0, n - 1
  while l <= r:
    m = (l + r) // 2
    if B[j] >= P[m]:
      l = m + 1
      c = m + 1
    else:
      r = m - 1
  l, r = 0, min(r + 1, n - 1)
  p = c
  if p == 0:
    print(c,end=' ')
  else:
    while l <= r:
      m = (l + r) // 2
      if A[j] <= P[m]:
        r = m - 1
      else:
        c = p - (m + 1)
        l = m + 1
    print(c,end=' ')