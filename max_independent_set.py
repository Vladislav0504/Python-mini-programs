def DFS(v,p,T,f,g):
  global W,n
  f[v], g[v] = W[v], 0
  E = []
  if v >= 1:
    E.append(T[v - 1][0])
  for i in range(n):
    if T[i][0] == v:
      E.append(i + 1)
  for u in E:
    if u != p:
      DFS(u,v,T,f,g)
      f[v] += g[u]
      g[v] += max(g[u],f[u])
n = int(input())
T = []
W = [0]
g = [-10**4-1] * (n + 1)
f = [-10**4-1] * (n + 1)
for i in range(n):
  T.append([int(j) for j in input().split()])
  W.append(T[i][1])
DFS(0,0,T,f,g)
print(max(f[0],g[0]))