from sys import stdin
def BFS(N, x, edges):
    Q = [x - 1]
    d = [-1] * N
    d[x - 1] = 0
    while Q:
        v = Q.pop(0)
        for u in edges[v]:
            if d[u] == -1:
                d[u] = d[v] + 1
                Q.append(u)
    return d
N, x = map(int, input().split())
edges = [[] for i in range(N)]
for i, line in enumerate(stdin):
    for j, elem in enumerate(line.split()):
        if int(elem):
            edges[i].append(j)
print(*BFS(N, x, edges))