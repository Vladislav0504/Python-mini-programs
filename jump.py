class Solution:
    def jump(self, arr: list) -> int:
        jumps = [len(arr)] * len(arr)
        jumps[0] = 0
        M = 1
        for i, elem in enumerate(arr):
        	for j in range(M, elem + 1):
        		if i + j < len(arr) and jumps[i + j] > jumps[i] + 1:
        			jumps[i + j] = jumps[i] + 1
        	M = max(M - 1, elem)
        return jumps[-1]