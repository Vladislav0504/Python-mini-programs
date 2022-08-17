def Countsort(A,n,i):
  M = 0
  for j in range(n):
    A[j][i] = ord(A[j][i])
    M = max(A[j][i],M)
  C = [0] * (M + 1)
  for j in range(n):
    C[A[j][i]] = C[A[j][i]] + 1
  H = [0] * (M + 1)
  H[0] = 0
  for k in range(1,M + 1):
    H[k] = H[k - 1] + C[k - 1]
  B = [0] * n
  for j in range(n):
    B[H[A[j][i]]] = A[j]
    H[A[j][i]] = H[A[j][i]] + 1
  for j in range(n):
    A[j] = B[j]
    A[j][i] = chr(A[j][i])
  return A
def Digitsort(A,n,m,k):
  for i in range(m-1,m-k-1,-1):
    A = Countsort(A,n,i)
n,m,k = map(int, input().split())
A = [[] for i in range(n)]
for i in range(n):
  s = str(input())
  for j in range(m):
    A[i].append(s[j])
A1=Digitsort(A,n,m,k)
W = []
for i in range(n):
  W.append(str(A[i][0]))
  for j in range(1,m):
    W[i] += str(A[i][j])
for elem in W:
  print(elem)