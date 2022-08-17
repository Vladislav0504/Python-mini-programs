import sys, threading
sys.setrecursionlimit(2 * 10 ** 5)
def dfs(v, edges, visited):
    visited[v] = True
    for u, w in edges[v]:
        if not visited[u]:
            dfs(u, edges, visited)
def dfs2(v, edges, visited, k):
    visited[v] = True
    for u, w in edges[v]:
        if not visited[u] and w == k:
            dfs2(u, edges, visited, k)
def main():
    n, m, q = map(int, input().split())
    edges = [set() for i in range(n)]
    for i, line in enumerate(sys.stdin):
        v, u, t = map(int, line.split())
        edges[v - 1].add((u - 1, t))
        edges[u - 1].add((v - 1, t))
        if i == m - 1:
            break
    visited = [False] * n
    dfs(0, edges, visited)
    ind = 0
    for el in visited:
        if not el:
            ind = 1
    if ind == 0:
        k1, k2 = 0, 0
        i = 0
        visited = [False] * n
        while i <= n - 1:
            dfs2(i, edges, visited, 0)
            k1 += 1
            if i == n - 1:
                break
            for j in range(i + 1, n):
                if not visited[j]:
                    i = j
                    break
                elif j == n - 1:
                    i = n
                    break
        visited = [False] * n
        i = 0
        while i <= n - 1:
            dfs2(i, edges, visited, 1)
            k2 += 1
            if i == n - 1:
                break
            for j in range(i + 1, n):
                if not visited[j]:
                    i = j
                    break
                elif j == n - 1:
                    i = n
                    break
        k1 -= 1
        k2 = n - 1 - (k2 - 1)
    for ai in sys.stdin:
        if ind == 1 or n - 1 - int(ai) > k2 or n - 1 - int(ai) < k1:
            print('NO')
        else:
            print('YES')
threading.stack_size(1 << 27)
thread = threading.Thread(target=main)
thread.start()
thread.join()