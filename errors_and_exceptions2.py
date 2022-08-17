import sys
n = int(input())
D = dict()
k = 0
for line in sys.stdin:
  k += 1
  s = line.split()
  D[s[0]] = [] if len(s) == 1 else s[2:len(s)]
  if k == n:
    break
m = int(input())
k = 0
lst = []
for line in sys.stdin:
  s = line.split()
  k += 1
  lst.append(s[0])
  if k == m:
    break
x = []
for i in range(len(lst) - 1,-1,-1):
  s = D[lst[i]]
  while len(s) > 0:
    h = 0
    for j in range(i - 1,-1,-1):
      if lst[j] in s and lst[i] not in x:
        x.append(lst[i])
        h = 1
        break
    s1 = []
    if h == 1:
      break
    else:
      for elem in s:
        for el in D[elem]:
          if el not in s1:
            s1.append(el)
    s = s1
for elem in x[::-1]:
  print(elem)