t = int(input())
for i in range(t):
  p = [int(i) for i in input().split()]
  q = p[0] - p[1] - p[2] + p[3]
  print(q)