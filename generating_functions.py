n = int(input())
a0, a1, s = 1, 1, 1
for j in range(1, n):
  a0, a1 = a1, (2 * a1 + s) % 1000000007
  s = (s + a0) % 1000000007
print(a1)