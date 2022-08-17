from sys import stdin
from collections import deque
def bfs(s, N, edges, C, F):
    Q = deque([s])
    d = [-1] * N
    d[s - 1] = 0
    while Q:
        v = Q.popleft()
        for u in edges[v]:
            if d[u - 1] == -1 and C[(v, u)] > F[(v, u)]:
                d[u - 1] = d[v - 1] + 1
                Q.append(u)
    return d
def dfs(v, t, flow, d, edges, C, F):
    if v == t:
        return flow
    for u in edges[v]:
        if d[u - 1] == d[v - 1] + 1 and C[(v, u)] > F[(v, u)]:
            delta1 = dfs(u, t, min(flow, C[(v, u)] - F[(v, u)]), d, edges, C, F)
            if delta1 > 0:
                F[(v, u)] += delta1
                F[(u, v)] -= delta1
                return delta1
    return 0
def dinic(s, N, edges, C, F):
    f = 0
    while True:
        d = bfs(s, N, edges, C, F)
        if d[-1] == -1:
            break
        while True:
            flow = dfs(s, N, 2 * 10 ** 4, d, edges, C, F)
            if flow > 0:
                f += flow
            else:
                break
    return f
def main():
    N = int(input())
    M = int(input())
    edges = {i: set() for i in range(1, N + 1)}
    C, lst, F = {}, {}, {}
    C2, F2 = [0] * M, [0] * M
    for i, line in enumerate(stdin):
        A, B, C1 = map(int, line.split())
        lst[(A, B)] = lst.get((A, B), []) + [i]
        edges[A].add(B)
        edges[B].add(A)
        C[(A, B)] = C.get((A, B), 0) + C1
        C[(B, A)] = C.get((B, A), 0) + C1
        F[(A, B)] = 0
        F[(B, A)] = 0
        C2[i] = C1 
    print(dinic(1, N, edges, C, F))
    for elem in F:
        while F[elem] > 0:
            if elem in lst:
                for el in lst[elem]:
                    delta = min(C2[el] - F2[el], F[elem])
                    if C2[el] > F2[el]:
                        F2[el] += delta
                    F[elem] -= delta
                    if F[elem] == 0:
                        break
            if F[elem] > 0:
                for el in lst[(elem[1], elem[0])]:
                    delta = min(C2[el] + F2[el], F[elem])
                    if C2[el] > -F2[el]:
                        F2[el] -= delta
                    F[elem] -= delta
                    if F[elem] == 0:
                        break
    for el in F2:
        print(el)
if __name__ == '__main__':
    main()