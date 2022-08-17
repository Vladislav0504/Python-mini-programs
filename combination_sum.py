T = []
class Solution:
    def combinationSum(self, nums: list, target: int, lst = []) -> list:
    	global T
    	nums.sort()
    	if nums[0] == 0:
    		nums = nums[1:]
    	s = [tuple(lst) for i in range(len(nums))]
    	for i, elem in enumerate(nums):
    		D = target
    		D -= elem
    		if D >= elem:
    			self.combinationSum(nums[i:], D, list(s[i]) + [elem])
    		elif D == 0:
    			T.append(list(s[i]) + [elem])
    	return T