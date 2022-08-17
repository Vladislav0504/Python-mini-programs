def NextSet(a, n):
	j = n - 2
	while j != -1 and a[j] >= a[j + 1]:
		j -= 1
	if j == -1:
		return False
	k = n - 1
	while a[j] >= a[k]:
		k -= 1
	a[j], a[k] = a[k], a[j]
	l, r = j + 1, n - 1
	while l < r:
		a[l], a[r] = a[r], a[l]
		l += 1
		r -= 1
	return True
class Solution:
    def permutations(self, nums: list) -> list:
    	nums.sort()
    	T = [tuple(nums)]
    	while NextSet(nums, len(nums)):
    	    T.append(tuple(nums)) 
    	return T  