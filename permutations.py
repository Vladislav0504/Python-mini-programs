from itertools import *
n, k = map(int, input().split())
s = ''
for i in range(n):
  s += str(i)
for i in permutations(s, k):
  for elem in i:
  	print(elem, end=' ')
  print()  