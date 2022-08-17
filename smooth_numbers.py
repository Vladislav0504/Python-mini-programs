def Sum(N):
  A = [[0 for i in range(10)] for j in range(N)]
  A[0] = [0,1,1,1,1,1,1,1,1,1]
  for j in range(1,N):
    for i in range(10):
      if i == 0:
        A[j][i] = A[j - 1][i] + A[j - 1][i + 1]
      elif i == 9:
        A[j][i] = A[j - 1][i - 1] + A[j - 1][i]
      else:
        A[j][i] = A[j - 1][i - 1] + A[j - 1][i] + A[j - 1][i + 1]
  return sum(A[N - 1])
N = int(input())
print(Sum(N))