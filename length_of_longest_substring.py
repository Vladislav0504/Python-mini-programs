class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    	P = {} # где каждый символ алфавита был ранее
    	best = 0
    	M = 0 # длина максимальной подстроки уникальных символов, заканчивающаяся на i-ом элементе строки
    	for elem in set(s):
    		P[elem] = -1
    	for i in range(len(s)):
    		M = min(M + 1, i - P[s[i]])
    		best = max(best, M)
    		P[s[i]] = i
    	return best