import sys#, threading
sys.setrecursionlimit(2 * 10 ** 5)
INF = 2 * 10 ** 12
class priority_queue(list):
    p = []
    def sift_up(self, i):
        while i > 0 and self[i][0] < self[(i - 1) // 2][0]:
            self[i], self[(i - 1) // 2] = self[(i - 1) // 2], self[i]
            self.p[self[i][1]], self.p[self[(i - 1) // 2][1]] = self.p[self[(i - 1) // 2][1]], self.p[self[i][1]]
            i = (i - 1) // 2
        return i
    def push(self, d, num):
        self.append([d, num])
        self.p.append(len(self) - 1)
        self.sift_up(len(self) - 1)
    def sift_down(self, i):
        while 2 * i + 1 <= len(self) - 1:
            j = 2 * i + 1
            if 2 * i + 2 <= len(self) - 1 and self[j][0] > self[2 * i + 2][0]:
                j = 2 * i + 2
            if self[i][0] <= self[j][0]:
                break
            self[i], self[j] = self[j], self[i]
            self.p[self[i][1]], self.p[self[j][1]] = self.p[self[j][1]], self.p[self[i][1]]
            i = j
    def extract_min(self):
        if self:
            self[0], self[-1] = self[-1], self[0]
            self.p[self[0][1]], self.p[self[-1][1]] = self.p[self[-1][1]], self.p[self[0][1]]
            elem = self.pop()
            self.p[elem[1]] = 'del'
            self.sift_down(0)
            return elem
    def decrease_key(self, num, k):
        if self.p[num] != 'del':
            self[self.p[num]][0] = min(self[self.p[num]][0], k)
            self.sift_up(self.p[num])
def bin_search(problems, i):
    l, r = i + 1, len(problems) - 1
    ind = len(problems)
    while l <= r:
        m = (l + r) // 2
        if problems[i][1] <= problems[m][0]:
            ind = m
            r = m - 1
        else:
            l = m + 1
    return ind
def dfs(v, t, flow, edges, visited, fi, cap, prev):
    if v == t:
        return flow
    visited[v] = True
    for u, c in edges[v]:
        if not visited[u] and cap[v][u] > 0 and c + fi[v] - fi[u] == 0:
            delta = dfs(u, t, min(flow, cap[v][u]), edges, visited, fi, cap, prev)
            if delta > 0:
                prev[u] = (v, c)
                cap[v][u] -= delta
                cap[u][v] += delta
                return delta
    return 0
def bellman_ford(s, t, cap, edges):
    d = [INF] * (t + 1)
    d[s] = 0
    for i in range(len(d) - 1):
        for v in range(len(d)):
            for u, c in edges[v]:
                if cap[v][u] > 0 and d[v] != INF and d[u] > d[v] + c:
                    d[u] = d[v] + c
    return d
def dijkstra(s, t, cap, edges, fi):
    d = [INF] * (t + 1)
    d[s] = 0
    S = priority_queue()
    S.p.clear()
    for i in range(t + 1):
        S.push(d[i], i)
    while True:
        v = S.extract_min()
        if v is None or d[v[1]] == INF:
            break
        for u, c in edges[v[1]]:
            if cap[v[1]][u] > 0:
                min_val = d[v[1]] + c + fi[v[1]] - fi[u]
                if d[u] > min_val:
                    d[u] = min_val
                    S.decrease_key(u, min_val)
    for i in range(t + 1):
        d[i] = min(d[i] + fi[i], INF)
    return d
def min_cost_flow(cap, edges, s, t, k, problems):
    prev = [-1] * (t + 1)
    fi = bellman_ford(s, t, cap, edges)
    cost_f = 0
    f = 0
    lst = [0] * ((t - 1) // 2)
    while f < k:
        visited = [False] * (t + 1)
        delta_f = dfs(s, t, (t - 1) // 2, edges, visited, fi, cap, prev)
        if delta_f > 0:
            current, cost = t, 0
            while current != s:
                cost += prev[current][1]
                if prev[current][1] < 0:
                    lst[problems[current // 2 - 1][3]] = 1
                elif prev[current][1] > 0:
                    lst[problems[(current + 1) // 2 - 1][3]] = 0
                current = prev[current][0]
            cost_f += delta_f * cost
            f += delta_f
            fi = dijkstra(s, t, cap, edges, fi)
        else:
            break
    return lst
def main():
    n, k = map(int, input().split())
    edges = {i: set() for i in range(2 * n + 2)}
    problems = [0] * n
    cap = [[0 for i in range(2 * n + 2)] for j in range(2 * n + 2)]
    for i, line in enumerate(sys.stdin):
        s, t, c = map(int, line.split())
        problems[i] = (s, s + t, -c, i)
    if k >= n:
        print(*([1] * n))
    else:
        problems.sort()
        for i in range(1, n + 1):
            edges[0].add((2 * i - 1, 0))
            edges[2 * i - 1].add((0, 0))
            cap[0][2 * i - 1] = 1
            edges[2 * i - 1].add((2 * i, problems[i - 1][2]))
            edges[2 * i].add((2 * i - 1, -problems[i - 1][2]))
            cap[2 * i - 1][2 * i] = 1
            edges[2 * i].add((2 * n + 1, 0))
            edges[2 * n + 1].add((2 * i, 0))
            cap[2 * i][2 * n + 1] = 1
            edges[2 * i - 1].add((2 * i + 1, 0))
            edges[2 * i + 1].add((2 * i - 1, 0))
            cap[2 * i - 1][2 * i + 1] = k
            if i != n:
                m = bin_search(problems, i - 1)
                if m <= n - 1:
                    edges[2 * i].add((2 * m + 1, 0))
                    edges[2 * m + 1].add((2 * i, 0))
                    cap[2 * i][2 * m + 1] = 1
        print(*min_cost_flow(cap, edges, 0, 2 * n + 1, k, problems))
if __name__ == '__main__':
    main()
#threading.stack_size(1 << 27)
#thread = threading.Thread(target=main)
#thread.start()
#thread.join()