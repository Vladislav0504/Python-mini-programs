import sys
def get_degree(v, graph):
  degree = 0
  for (x, y) in graph:
    if v == x or v == y:
      degree += 1
  return degree
def get_edge_and_index(v, graph):
  edge = ();
  index = -1
  for i in range(len(graph)):
    if (v == graph[i][0] or v == graph[i][1]):
      edge, index = graph[i], i
      break
  return index, edge
def find_eulerian_tour(graph):
  stack = [];
  tour = []
  stack.append(graph[0][0])
  while len(stack) > 0:
    v = stack[len(stack) - 1]
    degree = get_degree(v, graph)
    if degree == 0:
      stack.pop()
      tour.append(v)
    else:
      index, edge = get_edge_and_index(v, graph)
      graph.pop(index)
      stack.append(edge[1] if v == edge[0] else edge[0])
  return tour
def DFS(v):
  global visited, d
  visited[v - 1] = 1
  for w in d[v]:
  	if visited[w - 1] == 0:
  	  DFS(w)
def Euler(d):
  global v, visited, graph
  for key in d.keys():
  	if len(d[key]) % 2 == 1:
  	  return ['NONE']
  c, s, V = 0, 0, 1
  while s < v:
  	DFS(V)
  	c += 1
  	if c > 1:
  	  return ['NONE']
  	s += 1
  	for i in range(s, v):
  	  if visited[i] == 0:
  	  	V, s = i + 1, i
  	  	break
  	  if i == v - 1:
  	    s = v
  return find_eulerian_tour(graph)[1:]
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
print(*Euler(d))