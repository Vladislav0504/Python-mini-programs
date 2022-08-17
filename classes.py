n = int(input())
D = dict()
for i in range(n):
  s = [j for j in str(input()).split()]
  D[s[0]] = [s[0]]
  if len(s) > 1:
    l = len(s) - 1
    for j in range(2,l + 1):
      D[s[0]].append(s[j])
    for i in range(1,l):
      if D[s[0]][i] in D.keys():
        for elem in D[D[s[0]][i]]:
          if elem not in D[s[0]]:
            D[s[0]].append(elem)
    for elem in D.keys():
      if (elem != s[0]) and (s[0] in D[elem]):
        for el in D[s[0]]:
          if el not in D[elem]:
            D[elem].append(el)
q = int(input())
for i in range(q):
  s0,s1 = str(input()).split()
  if s0 in D[s1]:
    print('Yes')
  else:
    print('No')
