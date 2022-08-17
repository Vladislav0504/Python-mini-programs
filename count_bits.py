class Solution:
    def countBits(self, num: int) -> list:
    	D = [0] * (num + 1)
    	for i in range(1, num + 1):
    		D[i] = D[i // 2] + i % 2
    	return D