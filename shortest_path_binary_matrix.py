from collections import deque
def bfs(s, N, edges):
    Q = deque([s])
    d = [-1] * (N + 1)
    d[s] = 1
    while Q:
        v = Q.popleft()
        for u in edges[v]:
            if d[u] == -1:
                d[u] = d[v] + 1
                Q.append(u)
    return d[N]
class Solution:
    def shortestPathBinaryMatrix(self, grid: list) -> int:
    	edges = {i: set() for i in range(len(grid)**2)}
    	lst = {}
    	k = 0
    	for i, elem in enumerate(grid):
    		for j, el in enumerate(elem):
    			lst[(i, j)] = k
    			k += 1
    	for i, elem in enumerate(grid):
    		for j, el in enumerate(elem):
    			if grid[i][j] == 0:
    				for k1 in range(-1, 2):
    					for k2 in range(-1, 2):
    						if 0 <= i + k1 < len(grid) and 0 <= j + k2 < len(grid) and grid[i + k1][j + k2] == 0 and lst[(i + k1, j + k2)] != lst[(i, j)]:
    							edges[lst[(i, j)]].add(lst[(i + k1, j + k2)])
    	return bfs(0, len(grid)**2 - 1, edges)