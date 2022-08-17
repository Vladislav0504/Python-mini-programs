def RMQSparseTable(L, R):
  global h, f
  if R == L:
    return f[L - 1][0]
  elif R > L:
    t = h[R - L - 1]
    return min(f[L - 1][t], f[R - 2**t][t])
  else:
    t = h[L - R - 1]
    return min(f[R - 1][t], f[L - 2**t][t])
n, m, a1 = map(int, input().split())
h = [0] * n
for i in range(1, n):
  h[i] = h[(i + 1) // 2 - 1] + 1
f = [[-1 for j in range(h[n - 1] + 1)] for i in range(n)]
f[0][0] = a1
for i in range(1, n):
  f[i][0] = (23 * f[i - 1][0] + 21563) % 16714589
for k in range(1, h[n - 1] + 1):
  for i in range(n):
    f[i][k] = f[i][k - 1]
    if i + 2**(k - 1) < n:
      f[i][k] = min(f[i][k], f[i + 2**(k - 1)][k - 1])
u, v = map(int, input().split())
for j in range(1, m):
  r = RMQSparseTable(u, v)
  u, v = ((17 * u + 751 + r + 2 * j) % n) + 1, ((13 * v + 593 + r + 5 * j) % n) + 1
print(u, v, RMQSparseTable(u, v))