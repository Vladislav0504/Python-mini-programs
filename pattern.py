def Pattern(A,B):
  n = len(A)
  m = len(B)
  f = bool(1)
  k = -1
  for i in range(n):
    if A[i] != '*':
      f = False
      k = i
      break
  if m == 0 and f:
    return 'YES'
  elif m == 0 or n == 0:
    return 'NO'
  D = [[0 for j in range(m)] for i in range(n)]
  if A[0] == B[0] or A[0] == '*' or A[0] == '?':
    D[0][0] = 1
  for j in range(1,m):
    if A[0] == '*':
      D[0][j] = 1
  for i in range(1,n):
    if D[i - 1][0] == 1 and (A[i] == '*' or k == -1 or i <= k and (A[i] == B[0] or A[i] == '?')):
      D[i][0] = 1
  for i in range(1,n):
    for j in range(1,m):
      if A[i] == '*':
        D[i][j] = max(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1])
      elif A[i] == '?' or A[i] == B[j]:
        D[i][j] = D[i - 1][j - 1]
      else:
        D[i][j] = 0
  if D[n - 1][m - 1] == 1:
    return 'YES'
  else:
    return 'NO'
A = [i for i in input()]
B = [i for i in input()]
D = Pattern(A,B)
print(D)