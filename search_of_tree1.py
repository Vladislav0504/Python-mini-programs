import sys
def Search(v, h):
  global d, S, visited, s, lst
  S.pop(0)
  for w in d[v]:
  	if visited[w] == 0:
  	  visited[w] = 1
  	  s += 1
  	  S.append([w, h + 1])
  	  lst[w] = h + 1
V, E = map(int, input().split())
d = {i: [] for i in range(V)}
ind, s = 0, 1
lst = [0 for i in range(V)]
for line in sys.stdin:
  v1, v2 = map(int, line.split())
  d[v1].append(v2)
  d[v2].append(v1)
  ind += 1
  if ind >= E:
  	break
S = [[0, 0]]
visited = [1] + [0] * (V - 1)
while s < V:
  Search(*S[0])
for el in lst:
  print(el, end=' ')