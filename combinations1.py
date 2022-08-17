def NextSet(a, n, m):
	k = m
	for i in range(k - 1, -1, -1):
		if a[i] < n - k + i + 1:
			a[i] += 1
			for j in range(i + 1, k):
				a[j] = a[j - 1] + 1
			return True
	return False
class Solution:
    def combine(self, n: int, k: int) -> list:
    	a = [i for i in range(1, n + 1)]
    	T = [tuple(a[:k])]
    	if n >= k:
    		while NextSet(a, n, k):
    			T.append(tuple(a[:k])) 
    	return T  