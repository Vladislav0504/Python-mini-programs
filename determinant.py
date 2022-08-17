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
n = int(input())
A = np.array([[float(a) for a in input().split()] for j in range(n)])
print(round(Det(A,n)))