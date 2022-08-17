import sys
def DFS(v, color):
  global visited, d
  visited[v - 1] = color
  for w in d[v]:
  	if visited[w - 1] == 0:
  	  DFS(w, -color)
def Bichromatic(graph):
  global visited
  for el in graph:
  	if visited[el[0] - 1] == visited[el[1] - 1]:
  	  return 'NO'
  return 'YES'
v, e = map(int, input().split())
d = {i: [] for i in range(1, v + 1)}
ind = 0
graph = []
for line in sys.stdin:
  v1, v2 = map(int, line.split())
  graph.append((v1, v2))
  d[v1].append(v2)
  d[v2].append(v1)
  ind += 1
  if ind >= e:
  	break
visited = [0] * v
s, V = 0, 1
while s < v:
  DFS(V, 1)
  s += 1
  for i in range(s, v):
  	if visited[i] == 0:
  	  V, s = i + 1, i
  	  break
  	if i == v - 1:
  	  s = v
print(Bichromatic(graph))