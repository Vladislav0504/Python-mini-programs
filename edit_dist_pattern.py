def diff(a,b):
  if a == b:
    return 0
  else:
    return 1
def EditDistBottomUp(A,B):
  n = len(A)
  m = len(B)
  D = [[0 for j in range(m + 1)] for i in range(n + 1)]
  for i in range(n + 1):
    D[i][0] = i
  for j in range(1,m + 1):
    D[0][j] = j
  for i in range(1,n + 1):
    for j in range(1,m + 1):
      D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + diff(A[i - 1], B[j - 1]))
  return D[n][m]
A = [i for i in input()]
B = [i for i in input()]
D = EditDistBottomUp(A,B)
print(D)