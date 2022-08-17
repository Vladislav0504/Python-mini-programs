from collections import deque
def bfs(s, N, edges):
    Q = deque([s])
    d = [-1] * N
    d2 = [-1] * N
    d[s] = 0
    d2[s] = 0
    while Q:
        v = Q.popleft()
        for u, col in edges[v]:
        	if d[u] == -1 and d2[v] != -1 and col == 1:
        		d[u] = d2[v] + 1
        		Q.append(u)
        	elif d2[u] == -1 and d[v] != -1 and col == 0:
        		d2[u] = d[v] + 1
        		Q.append(u)
    return d, d2
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: list, blue_edges: list) -> list:
    	edges = [set() for i in range(n)]
    	for el in red_edges:
    		edges[el[0]].add((el[1], 1))
    	for el in blue_edges:
    		edges[el[0]].add((el[1], 0))
    	d, d2 = bfs(0, n, edges)
    	D = d
    	for i in range(n):
    		if d2[i] >= 0:
    			if D[i] != -1:
    				D[i] = min(d2[i], D[i])
    			else:
    				D[i] = d2[i]
    	return D