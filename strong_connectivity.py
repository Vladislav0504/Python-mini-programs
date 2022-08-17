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
  n, m = map(int, input().split())
  lst = [[] for i in range(n)]
  lst2 = [[] for i in range(n)]
  p, V = 0, 0
  for line in sys.stdin:
    v1, v2 = map(int, line.split())
    if (v2 - 1) not in lst[v1 - 1] and v1 != v2:
  	  lst[v1 - 1].append(v2 - 1)
  	  lst2[v2 - 1].append(v1 - 1)
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
  c, k = 0, 0
  for i in range(n - 1, -1, -1):
  	v = s[i]
  	if component[v] == -1:
  	  SCC(v, c, component, lst2)
  	  c += 1
  edges = [[] for i in range(c)]
  for i in range(n):
  	for v in lst[i]:
  	  if component[i] != component[v] and component[v] not in edges[component[i]]:
  	  	edges[component[i]].append(component[v])
  	  	k += 1
  print(k)
if __name__ == '__main__':
  main()