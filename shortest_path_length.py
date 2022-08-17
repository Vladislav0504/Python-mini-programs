from collections import deque
def bfs(s, edges):
    Q = deque([s])
    d = [-1] * len(edges)
    d[s] = 0
    while Q:
        v = Q.popleft()
        for u in edges[v]:
        	if d[u] == -1:
        		d[u] = d[v] + 1
        		Q.append(u)
    return d
def travelling_salesman(a):
    n = len(a)
    f = [[10**9] * n for i in range(2**n)]
    for v in range(n):
        f[2**v][v] = 0
    for A in range(1, 2**n):
        if A & (A - 1) != 0:
            for v in range(n):
                if A & 2**v != 0:
                    for u in range(n):
                        if A & 2**u != 0 and u != v:
                            if f[A][v] > f[A & ~2**v][u] + a[u][v]:
                                f[A][v] = f[A & ~2**v][u] + a[u][v]
    return min(f[2**n - 1])
class Solution:
    def shortestPathLength(self, graph: list) -> int:
        A = [bfs(i, graph) for i in range(len(graph))]
        return travelling_salesman(A)