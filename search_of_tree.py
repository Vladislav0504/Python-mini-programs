import sys, threading
sys.setrecursionlimit(2 * 10**5)
threading.stack_size(1 << 27)
def DFS(v, visited, lst, c):
  visited[v - 1] = c
  for w in lst[v - 1]:
  	if visited[w - 1] == 0:
  	  DFS(w, visited, lst, c)
def main():
  n, m = map(int, input().split())
  lst = [[] for i in range(n)]
  c, s, V = 0, 0, 1
  for line in sys.stdin:
    v1, v2 = map(int, line.split())
    if v2 not in lst[v1 - 1] and v1 != v2:
  	  lst[v1 - 1].append(v2)
  	  lst[v2 - 1].append(v1)
  visited = [0] * n
  while s < n:
    c += 1
    DFS(V, visited, lst, c)
    s += 1
    for i in range(s, n):
  	  if visited[i] == 0:
  	    V, s = i + 1, i
  	    break
  	  if i == n - 1:
  	    s = n
  print(c)
  print(*visited)
thread = threading.Thread(target = main)
thread.start()
thread.join()