class Solution:
    def maxProfit(self, prices: list) -> int:
    	P = 0
    	m, M = prices[0], prices[0]
    	im, iM = 0, 0
    	for i in range(1, len(prices)):
    		if prices[i] < m:
    			m, im = prices[i], i
    		elif prices[i] > M or iM < im:
    			M, iM = prices[i], i
    		if M - m > P and im < iM:
    			P = M - m
    	return P