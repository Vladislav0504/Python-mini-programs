class Solution:
  def peakIndexInMountainArray(self, nums):
    l, r = 0, len(nums)
    while l < r:
      m = (l + r) // 2
      if nums[m] >= nums[m + 1]:
        if nums[m] > nums[m - 1]:
          return m
        else:
          r = m
      else:
        l = m + 1