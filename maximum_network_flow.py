import sys
def DFS(v, delta, visited, t, edges, C):
  if v == t:
  	return delta
  visited[v] = True
  if v in edges.keys():
  	for child in edges[v]:
  	  if visited[child] == False and C[(v, child)] > 0:
  	  	delta1 = DFS(child, min(delta, C[(v, child)]), visited, t, edges, C)
  	  	if delta1 > 0:
  	  	  C[(v, child)] -= delta1
  	  	  C[(child, v)] += delta1
  	  	  return delta1
  return 0
def main():
  with open('C:\\Users\\admin\\Downloads\\max_flow.txt', 'r') as f:
  	reader = (tuple(map(int, line.split())) for line in f)#sys.stdin)
  	v, e = next(reader)
  	edges = {}
  	C = {}
  	for el in reader:
  	  if el[0] != el[1]:
  	  	edges[el[0]] = edges.get(el[0], []) + [el[1]]
  	  	edges[el[1]] = edges.get(el[1], []) + [el[0]]
  	  	C[(el[0], el[1])] = C.get((el[0], el[1]), 0) + el[2]
  	  	C[(el[1], el[0])] = C.get((el[1], el[0]), 0)
  max_flow = 0
  while True:
  	visited = [False] * v
  	delta = DFS(0, 50, visited, v - 1, edges, C)
  	if delta > 0:
  	  max_flow += delta
  	else:
  	  break
  print(max_flow)
if __name__ == '__main__':
  main()