import sys
sys.setrecursionlimit(10000)
def DFS(v, visited, d, tree, K1, K2):
  global k
  visited[v] = 1
  for w in d[v]:
  	if visited[w] == 0:
  	  tree[v].append(w)
  	  tree[w] = [v]
  	  k += 1
  	  K1[k], K2[w] = w, k
  	  DFS(w, visited, d, tree, K1, K2)
def main():
  with open('C:\\Users\\admin\\Downloads\\cutpoints.txt', 'r') as f:
  	edges = list(tuple(map(int, line.split())) for line in f)#sys.stdin)
  d = {}
  for el in edges:
  	d[el[0]] = d.get(el[0], []) + [el[1]] 
  	d[el[1]] = d.get(el[1], []) + [el[0]] 
  visited = [0] * len(d)
  tree = {0: [-1]}
  K1, K2 = {1: 0}, {0: 1}
  DFS(0, visited, d, tree, K1, K2)
  L = {}
  for i in range(len(K1), 0, -1):
  	L[K1[i]] = i
  	m = 10**5
  	for el in tree[K1[i]][1:]:
  	  m = min(m, L[el])
  	  L[K1[i]] = min(L[K1[i]], m)
  	for el in d[K1[i]]:
  	  if i > K2[el] and el != tree[K1[i]][0]:
  	  	L[K1[i]] = min(L[K1[i]], K2[el])
  cutpoints = []
  if len(tree[0]) > 2:
  	cutpoints.append(0)
  for el in tree.keys():
  	if el != 0:
  	  for child in tree[el][1:]:
  	  	if L[child] >= K2[el]:
  	  	  cutpoints.append(el)
  	  	  break
  print(*cutpoints)
if __name__ == '__main__':
  k = 1
  main()