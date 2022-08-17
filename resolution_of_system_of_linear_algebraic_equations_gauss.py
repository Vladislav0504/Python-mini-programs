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
def res(Ab,n,m):
  i = 0
  el = 0 
  for j in range(min(n,m)):
    if Ab[i][j] == 0:
      el = i
      while Ab[i][j] == 0 and i != n - 1:
        i += 1
    if Ab[i][j] != 0:
      t = np.array(Ab[el])
      Ab[el] = Ab[i]
      Ab[i] = t
      i = el + 1
      for k in range(i,n):
        Ab[k] = Ab[k] - Ab[k][j]/Ab[el][j]*Ab[el]
      el = i
    else:
      i = el
  for j in range(i,n):
    if Ab[j][m] != 0:
      return 'NO'
  if i < m:
    return 'INF'
  else:
    print('YES')
    x = np.array([0.0 for t in range(m)])
    for t in range(m):
      T = np.array(Ab)
      T[:,t] = Ab[:,m]
      x[t] = Det(T,m)/Det(Ab,m)
      print(x[t],end=' ')
    return '' 
n, m = input().split()
n = int(n)
m = int(m)
Ab = np.array([[float(a) for a in input().split()] for j in range(n)])
print(res(Ab,n,m))