from sys import stdin
def Floyd(N, edges):
    inf = N * 100 + 1
    d = [[inf] * N for i in range(N)]
    for i in range(N):
        d[i][i] = 0
    for v in range(N):
        for u, w in edges[v]:
            d[v][u] = w
    for k in range(N):
        for v in range(N):
            for u in range(N):
                if d[v][k] != inf and d[k][u] != inf and d[v][k] + d[k][u] < d[v][u]:
                    d[v][u] = d[v][k] + d[k][u]
    return d
N = int(input())
edges = [[] for i in range(N)]
for i, line in enumerate(stdin):
    for j, elem in enumerate(line.split()):
        if int(elem):
            edges[i].append((j, int(elem)))
for line in Floyd(N, edges):
    print(*line)