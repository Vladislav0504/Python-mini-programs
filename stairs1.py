class Solution:
    def minCost(self, cost: list) -> int:
    	D = [0] * (len(cost) + 1)
    	for i in range(2, len(cost) + 1):
    		D[i] = min(D[i - 1] + cost[i - 1], D[i - 2] + cost[i - 2])
    	return D[len(cost)]