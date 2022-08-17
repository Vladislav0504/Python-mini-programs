import sys
sys.setrecursionlimit(2 * 10**5)
def DFS(v, used, lst, s):
  used[v] = True
  for u in lst[v]:
  	if not used[u]:
  	  DFS(u, used, lst, s)
  s.append(v)
def SCC(v, c, component, lst):
  component[v] = c
  for u in lst[v]:
  	if component[u] == -1:
  	  SCC(u, c, component, lst)
def main():
  n = int(input())
  m = int(input())
  lst = [[] for i in range(n)]
  lst2 = [[] for i in range(n)]
  p, V = 0, 0
  for line in sys.stdin:
    a, b = map(int, line.split())
    if (b - 1) not in lst[a - 1] and a != b:
  	  lst[a - 1].append(b - 1)
  	  lst2[b - 1].append(a - 1)
  used = [False] * n
  s = []
  while p < n:
    DFS(V, used, lst, s)
    p += 1
    for i in range(p, n):
  	  if not used[i]:
  	    V, p = i, i
  	    break
  	  if i == n - 1:
  	    p = n
  component = [-1] * n
  c = 0
  for i in range(n - 1, -1, -1):
  	v = s[i]
  	if component[v] == -1:
  	  SCC(v, c, component, lst2)
  	  c += 1
  edges = [[] for i in range(c)]
  safety = []
  for i in range(n):
  	for v in lst[i]:
  	  if component[i] != component[v] and component[v] not in edges[component[i]]:
  	  	edges[component[i]].append(component[v])
  for i in range(c):
  	if len(edges[i]) == 0:
  	  for j in enumerate(component):
  	  	if component[j[0]] == i:
  	  	  safety.append(j[0] + 1)
  	  	  break
  print(len(safety))
  print(*safety)
if __name__ == '__main__':
  main()