from sys import stdin
def dfs(v, t, flow, edges, C, visited):
    if v == t:
        return flow
    visited[v - 1] = True
    for u in edges[v]:
        if visited[u - 1] == False and C[(v, u)] > 0:
            delta1 = dfs(u, t, min(flow, C[(v, u)]), edges, C, visited)
            if delta1 > 0:
                C[(v, u)] -= delta1
                C[(u, v)] += delta1
                return delta1
    return 0
def dfs2(v, visited, edges, C, V1):
    visited[v - 1] = True
    V1.add(v)
    for u in edges[v]:
        if not visited[u - 1] and C[(v, u)] > 0:
            dfs2(u, visited, edges, C, V1)
def dfs3(v, visited, edges, V1, Lst, lst):
    visited[v - 1] = True
    for u in edges[v]:
        if u in V1:
            if (u, v) in lst:
                Lst.append(lst[(u, v)])
            else:
                Lst.append(lst[(v, u)])
        elif not visited[u - 1]:
            dfs3(u, visited, edges, V1, Lst, lst)
def ford_fulkerson(s, N, edges, C):
    max_flow = 0
    while True:
        visited = [False] * N
        delta = dfs(s, N, 2 * 10 ** 7, edges, C, visited)
        if delta > 0:
            max_flow += delta
        else:
            break
    return max_flow
def main():
    n, m = map(int, input().split())
    edges = {i: set() for i in range(1, n + 1)}
    C, lst = {}, {}
    visited = [False] * n
    V1 = set()
    for i, line in enumerate(stdin, 1):
        A, B, C1 = map(int, line.split())
        if A != B:
            lst[(A, B)] = i
            edges[A].add(B)
            edges[B].add(A)
            C[(A, B)] = C1
            C[(B, A)] = C1
    flow = ford_fulkerson(1, n, edges, C)
    dfs2(1, visited, edges, C, V1)
    visited = [False] * n
    Lst = []
    dfs3(n, visited, edges, V1, Lst, lst)
    print(len(Lst), flow)
    Lst.sort()
    print(*Lst)
if __name__ == '__main__':
    main()