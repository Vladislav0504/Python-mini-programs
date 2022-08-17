from collections import deque
def bfs(edges, points, m, n, coord_B):
	d = [[-1] * n for i in range(m)]
	Q = deque([points[0]])
	d[points[0][0]][points[0][1]] = 0
	while Q:
		v = Q.popleft()
		if v == points[1]:
			return True
		if v in edges:
			for u in edges[v]:
				if d[u[0]][u[1]] == -1 and u != coord_B:
					d[u[0]][u[1]] = d[v[0]][v[1]] + 1
					Q.append(u)
	return False
def bfs1(edges, points, m, n):
	d = {(points['S'], points['B']): 0}
	Q = deque([(points['S'], points['B'])])
	while Q:
		S, B = Q.popleft()
		if B in edges:
			for u in edges[B]:
				need_S = (2 * B[0] - u[0], 2 * B[1] - u[1])
				if 0 <= need_S[0] < m and 0 <= need_S[1] < n and bfs(edges, (S, need_S), m, n, B) and (need_S, u) not in d:
					d[(need_S, u)] = d[(S, B)] + 1
					Q.append((need_S, u))
					if u == points['T']:
						return d[(need_S, u)]
	return -1
class Solution:
    def minPushBox(self, grid: list) -> int:
        points = {'T': 0, 'B': 0, 'S': 0}
        graph = {}
        for i, elem in enumerate(grid):
        	for j, point in enumerate(elem):
        		if point != '#':
        			if point != '.':
        				points[point] = (i, j)
        			for delta in [-1, 1]:
        				if 0 <= i + delta < len(grid) and grid[i + delta][j] != '#':
        					graph[(i, j)] = graph.get((i, j), []) + [(i + delta, j)]
        				if 0 <= j + delta < len(grid[0]) and grid[i][j + delta] != '#':
        					graph[(i, j)] = graph.get((i, j), []) + [(i, j + delta)]
        return bfs1(graph, points, len(grid), len(grid[0]))