class Solution:
    def minAreaFreeRect(self, points: list) -> float:
    	points = [(el[0], el[1]) for el in points]
    	n = len(points)
    	S = 10**9
    	my_set = set(points)
    	for i in range(n):
    		x1, y1 = points[i]
    		for j in range(i + 1, n):
    			x2, y2 = points[j]
    			for p in points:
    				if p != points[i] and p != points[j] and (x2 - x1) * (p[0] - x1) + (y2 - y1) * (p[1] - y1) == 0:
    					if (p[0] + x2 - x1, p[1] + y2 - y1) in my_set:
    						S2 = ((y2 - y1)**2 + (x2 - x1)**2) * ((x1 - p[0])**2 + (y1 - p[1])**2)
    						if S2 < S**2:
    							S = S2**0.5
    	if S == 10**9:
    		return 0
    	return S