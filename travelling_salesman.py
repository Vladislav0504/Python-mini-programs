def TravellingSalesman(a,n):
  f = [[10**7 for j in range(n)] for i in range(2**n)]
  T = [[0 for j in range(n)] for i in range(2**n - 1)]
  for v in range(n):
    f[2**v][v] = 0
  for A in range(1,2**n):
    if A & (A - 1) != 0:
      for v in range(n):
        if A & 2**v != 0:
          for u in range(n):
            if A & 2**u != 0 and u != v:
              if f[A][v] > f[A & ~2**v][u] + a[u][v]:
                f[A][v] = f[A & ~2**v][u] + a[u][v]
                T[A - 1][v] = u
  t = min(f[2**n - 1])
  print(t)
  lst = []
  k = -1
  j = 2**n - 1
  for i in range(n):
    if f[2**n - 1][i] == t:
      k = i
      break
  lst.append(k + 1)
  l = 1
  while l < n:
    lst.append(T[j - 1][k] + 1)
    l += 1
    j, k = j - 2**k, T[j - 1][k]
  return lst
n = int(input())
A = [[int(j) for j in input().split()] for i in range(n)]
answer = TravellingSalesman(A,n)
for i in range(n):
  print(answer[i],end=' ')