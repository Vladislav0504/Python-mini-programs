def KnapsackWithoutRepsBU(M,n,m,c):
  D = [[0 for i in range(n + 1)] for w in range(M + 1)]
  for i in range(1,n + 1):
    for w in range(1,M + 1):
      D[w][i] = D[w][i - 1]
      if m[i - 1] <= w:
        if D[w - m[i - 1]][i - 1] + c[i - 1] > D[w][i]:
          D[w][i] = D[w - m[i - 1]][i - 1] + c[i - 1]
  lst = []
  m0 = M
  h = n
  while D[m0][h] > 0:
    if m0 >= m[h - 1]:
      if D[m0][h] == D[m0 - m[h - 1]][h - 1] + c[h - 1]:
        lst.append(h)
        m0 -= m[h - 1]
    h -= 1
  print(len(lst))
  return lst[::-1]
n, M = map(int, input().split())
m = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
C = KnapsackWithoutRepsBU(M,n,m,c)
for elem in C:
  print(elem,end=' ')