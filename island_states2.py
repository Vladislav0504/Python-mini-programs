def Cost(lst):
  global City
  if City[lst[0] - 1] == City[lst[1] - 1]:
    return 0
  else:
    if lst[0] % 2 == 0:
      return 2
    else:
      return 1
N, M = map(int, input().split())
City = [int(i) for i in input().split()]
Roads = {}
for i in range(M):
  a, b = map(int, input().split())
  if a not in Roads.keys():
    Roads[a] = [b]
  else:
    Roads[a].append(b)
  if b not in Roads.keys():
    Roads[b] = [a]
  else:
    Roads[b].append(a)
C = [2*10**5] * N
C[0] = 0
prev = [-1] * N
lst = [1]
l = 1
j = 1
if 1 not in Roads.keys():
  print('impossible')
else:
  while j <= l:
    t = lst[j - 1]
    for el in Roads[t]:
      if C[t - 1] + Cost([t, el]) < C[el - 1]:
        C[el - 1] = C[t - 1] + Cost([t, el])
        prev[el - 1] = t - 1
        lst.append(el)
        l += 1
    j += 1
  Cities = [N]
  if C[N - 1] == 2*10**5:
    print('impossible')
  else:
    h = N - 1
    while prev[h] != -1:
      Cities.append(prev[h] + 1)
      h = prev[h]
    Cities.reverse()
    print(C[N - 1],end=' ')
    print(len(Cities))
    for el in Cities:
      print(el,end=' ')