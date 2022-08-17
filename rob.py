class Solution:
    def rob(self, nums: list) -> int:
    	D = [nums[0]] * len(nums)
    	if len(nums) > 1:
    		D[1] = max(nums[1], nums[0])
    	for i in range(2, len(nums)):
    		D[i] = max(D[i - 1], D[i - 2] + nums[i])
    	return D[len(nums) - 1]