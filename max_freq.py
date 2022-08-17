class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    	strs = {}
    	for k in range(minSize, maxSize + 1):
    		i = 0
    		while i <= len(s) - k:
    			if len(set(s[i:i + k])) <= maxLetters:
    				strs[s[i:i + k]] = strs.get(s[i:i + k], 0) + 1
    			i += 1
    	if strs:
    		return max(strs.values())
    	return 0