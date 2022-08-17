def Sets(s, i, d, T, string):
	if i == len(string):
		T.append(''.join(string))
	else:
		for el in d[s[i]]:
			string[i] = el
			Sets(s, i + 1, d, T,string)
class Solution:
    def letterCombinations(self, digits: str) -> list:
    	global string
    	d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    	string = [elem for elem in digits]
    	T = []
    	Sets(digits, 0, d, T, string)
    	return T 