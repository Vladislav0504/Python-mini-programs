def BFS(N, x, y, edges):
    Q = [x - 1111]
    d = [-1] * N
    par = [-1] * N
    d[x - 1111], par[x - 1111] = 0, -2
    while Q:
        v = Q.pop(0)
        for u in edges[v]:
            if d[u] == -1:
                d[u] = d[v] + 1
                par[u] = v
                Q.append(u)
    lst, y = [y], y - 1111
    while par[y] != -2:
        lst.append(par[y] + 1111)
        y = par[y]
    return lst[::-1]
a = int(input())
b = int(input())
N = 8889
edges = [[] for i in range(N)]
for i in range(N):
    if i // 1000 < 8:
        edges[i].append(i + 1000)
    if i % 10 > 0:
        edges[i].append(i - 1)
    p1, p2 = i // 10 + 1000 * (i % 10), i // 1000 + 10 * (i % 1000)
    if i != p1 and p1 not in edges[i]:
        edges[i].append(p1)
    if i != p2 and p2 not in edges[i]:
        edges[i].append(p2)
print(*BFS(N, a, b, edges))