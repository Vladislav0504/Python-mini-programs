from sys import stdin
def DFS(v):
    global used, edges
    used[v] = True
    for u, w in edges[v]:
        if not used[u]:
            DFS(u)
def BellmanFord(k):
    global d, Bad_Cycle_vertex, edges, inf
    for i in range(len(d) - 1):
        for v in range(len(d)):
            for u, w in edges[v]:
                if d[v] != inf and d[u] > d[v] + w:
                    if k:
                        d[u] = d[v] + w
                    else:
                        Bad_Cycle_vertex[v] = True
n, m, s = map(int, input().split())
edges = [[] for i in range(n)]
M = 0
for line in stdin:
    v, u, w = map(int, line.split())
    if v != u or w < 0:
        M = max(M, w)
        edges[v - 1].append((u - 1, w))
inf = (n - 1) * M + 1
d = [inf] * n
d[s - 1] = 0
Bad_Cycle_vertex = [False] * n
used = [False] * n
BellmanFord(1)
BellmanFord(0)
for v in range(n):
    if Bad_Cycle_vertex[v]:
        DFS(v)
for v in range(n):
    if d[v] == inf:
        print('*')
    elif used[v]:
        print('-')
    else:
        print(d[v])