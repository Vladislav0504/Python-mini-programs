import numpy as np
def Det(A,n):
  det = 1
  for j in range(n):
    i = j
    while A[i][j] == 0:
      if i != n - 1:
        i += 1
      else:
        break
    if A[i][j] == 0:
      det = 0 
      break
    elif i != j:
      det = det*(-1)
      t = np.array(A[j])
      A[j] = A[i]
      A[i] = t
    for k in range(j+1,n):
      A[k] = A[k] - A[k][j]/A[j][j]*A[j]
    det = det*A[j][j]
  return det
def scal_prod(a,b):
  sum = 0
  for i in range(len(a)):
    sum += a[i]*b[i]
  return sum
n, m = input().split()
n = int(n)
m = int(m)
Ab = np.array([[float(a) for a in input().split()] for j in range(n)])
b = np.array([scal_prod(Ab[:,m],Ab[:,i]) for i in range(m)])
A = np.array([[scal_prod(Ab[:,i],Ab[:,j]) for j in range(m)] for i in range(m)])
D = np.array([0.0 for i in range(m)])
for i in range(m):
  T = np.array(A)
  T[:,i] = b
  D[i] = Det(T,m)
x = np.array([D[i]/Det(A,m) for i in range(m)])
for i in range(m):
  print(x[i],end=' ')