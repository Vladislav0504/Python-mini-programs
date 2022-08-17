def Balls(A):
  s = 0
  D = [[A[1],1]]
  l = 1
  for i in range(2,A[0] + 1):
    if A[i] == D[l - 1][0]:
      D[l - 1][1] += 1
    else:
      if D[l - 1][1] >= 3:
        s += D[l - 1][1]
        D.pop()
        l -= 1
        if A[i] == D[l - 1][0]:
          D[l - 1][1] += 1
        else:
          D.append([A[i],1])
          l += 1
      else:
        D.append([A[i],1])
        l += 1
  if D[l - 1][1] >= 3:
    s += D[l - 1][1]
  return s
A = [int(a) for a in input().split()]
print(Balls(A))