from itertools import *
k, n = map(int, input().split())
s = ''
for i in range(n):
  s += str(i)
for i in combinations(s, k):
  for elem in i:
  	print(elem, end=' ')
  print()  