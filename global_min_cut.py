from sys import stdin

def dfs(v, t, flow, C, F, visited):
    if v == t:
        return flow
    visited[v] = True
    for u in range(len(C)):
        if not visited[u] and C[v][u] > F[v][u]:
            delta1 = dfs(u, t, min(flow, C[v][u] - F[v][u]), C, F, visited)
            if delta1 > 0:
                F[v][u] += delta1
                F[u][v] -= delta1
                return delta1
    return 0
def dfs2(v, visited, C, F, V1):
    visited[v] = True
    V1.add(v)
    for u in range(len(C)):
        if not visited[u] and C[v][u] > F[v][u]:
            dfs2(u, visited, C, F, V1)
def dfs3(v, visited, C, V1, V2):
    visited[v] = True
    V2.add(v + 1)
    for u in range(len(C)):
        if C[v][u] and u in V1:
            continue
        elif C[v][u] and not visited[u]:
            dfs3(u, visited, C, V1, V2)
def ford_fulkerson(s, N, C, F):
    max_flow = 0
    while True:
        visited = [False] * len(C)
        delta = dfs(s, N, 5 * 10 ** 3, C, F, visited)
        if delta > 0:
            max_flow += delta
        else:
            break
    return max_flow
def main():
    n = int(input())
    C = [[0 for i in range(n)] for j in range(n)]
    visited = [False] * n
    V1 = set()
    for i, st in enumerate(stdin):
        for j in range(i + 1, n):
            if st[j] == '1':
                C[i][j] = 1
                C[j][i] = 1
    min_f, V = 2 * n ** 2, 1
    for v in range(1, n):
        F = [[0 for i in range(n)] for j in range(n)]
        flow = ford_fulkerson(0, v, C, F)
        if flow < min_f:
            min_f, V = flow, v
    F = [[0 for i in range(n)] for j in range(n)]
    flow = ford_fulkerson(0, V, C, F)
    dfs2(0, visited, C, F, V1)
    visited = [False] * n
    V2 = set()
    dfs3(V, visited, C, V1, V2)
    V1 = set(range(1, n + 1)).difference(V2)
    print(*V1)
    print(*V2)
if __name__ == '__main__':
    main()