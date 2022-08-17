class Solution:
    def minimum(self, f) -> float:
    	ans = min(f(0), f(1))
    	for i in range(1, 10000):
    		value = f(i / 10000)
    		if value < ans:
    			ans = value
    	return ans