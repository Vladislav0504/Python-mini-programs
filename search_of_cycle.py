import sys, threading
sys.setrecursionlimit(2 * 10**5)
threading.stack_size(1 << 27)
def DFS(v, visited, lst, Cycle, par):
  visited[v - 1] = 1
  for w in lst[v - 1]:
  	if visited[w - 1] == 0:
  	  par[w - 1] = v
  	  if DFS(w, visited, lst, Cycle, par):
  	  	return True
  	elif visited[w - 1] == 1:
  	  Cycle.append(v)
  	  while w != v:
  	  	Cycle.append(w)
  	  	for el in lst[w - 1]:
  	  	  if visited[el - 1] == 1:
  	  	  	w = el
  	  	  	break
  	  return True
  visited[v - 1] = 2
  lst[v - 1].clear()
  if par[v - 1] != -1:
  	lst[par[v - 1] - 1].remove(v)
def main():
  n, m = map(int, input().split())
  lst = [[] for i in range(n)]
  par = [-1 for i in range(n)]
  Cycle = []
  s, V = 0, 1
  for line in sys.stdin:
    v1, v2 = map(int, line.split())
    if v2 not in lst[v1 - 1] and v1 != v2:
  	  lst[v1 - 1].append(v2)
  visited = [0] * n
  while s < n:
    if DFS(V, visited, lst, Cycle, par):
      print('YES')
      print(*Cycle)
      break
    s += 1
    for i in range(s, n):
  	  if visited[i] == 0:
  	    V, s = i + 1, i
  	    break
  	  if i == n - 1:
  	    s = n
  if len(Cycle) == 0:
  	print('NO')
thread = threading.Thread(target = main)
thread.start()
thread.join()