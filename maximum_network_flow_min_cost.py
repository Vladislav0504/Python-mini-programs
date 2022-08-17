from sys import stdin

INF = 2 * 10 ** 5
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
def dfs(v, t, flow, edges, visited, fi, cap, prev):
    if v == t:
        return flow
    visited[v] = True
    for u, c in edges[v]:
        if not visited[u] and cap[(v, u, c)] > 0 and c + fi[v] - fi[u] == 0:
            delta = dfs(u, t, min(flow, cap[(v, u, c)]), edges, visited, fi, cap, prev)
            if delta > 0:
                prev[u] = (v, c)
                cap[(v, u, c)] -= delta
                cap[(u, v, -c)] += delta
                return delta
    return 0
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
            if cap[(v[1], u, c)] > 0:
                min_val = d[v[1]] + c + fi[v[1]] - fi[u]
                if d[u] > min_val:
                    d[u] = min_val
                    S.decrease_key(u, min_val)
    for i in range(t + 1):
        d[i] = min(d[i] + fi[i], INF)
    return d
def min_cost_flow(cap, edges, s, t):
    prev = [-1] * (t + 1)
    fi = [0] * (t + 1)
    fi = dijkstra(s, t, cap, edges, fi)
    cost_f = 0
    k = INF
    f = 0
    while f < INF:
        visited = [False] * (t + 1)
        delta_f = dfs(s, t, INF, edges, visited, fi, cap, prev)
        if delta_f > 0:
            current, cost = t, 0
            while current != s:
                cost += prev[current][1]
                current = prev[current][0]
            cost_f += delta_f * cost
            f += delta_f
            fi = dijkstra(s, t, cap, edges, fi)
        else:
            break
    return cost_f
def main():
    n, m = map(int, input().split())
    edges = {i: set() for i in range(n)}
    cap = {}
    for line in stdin:
        A, B, C, D = map(int, line.split())
        if A != B:
            edges[A - 1].add((B - 1, D))
            edges[B - 1].add((A - 1, -D))
            cap[(A - 1, B - 1, D)] = cap.get((A - 1, B - 1, D), 0) + C
            cap[(B - 1, A - 1, -D)] = 0
    print(min_cost_flow(cap, edges, 0, n - 1))
if __name__ == '__main__':
    main()