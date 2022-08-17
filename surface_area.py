class Solution:
    def surfaceArea(self, grid: list) -> int:
        ans = 0
        n = len(grid)
        for el in grid:
        	ans += 6 * sum(el)
        	el.append(0)
        grid.extend([[0] * (n + 1)])
        for i in range(n):
        	for j in range(n):
        		p = grid[i][j]
        		if p > 0:
        			ans -= 2 * (p - 1 + min(p, grid[i][j + 1]) + min(p, grid[i + 1][j]))
        return ans