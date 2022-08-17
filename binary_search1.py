class Solution:
  def search(self, nums, target: int):
    l, r = 0, len(nums) - 1
    ind = -1
    while l <= r:
      m = (l + r) // 2
      if nums[m] == target:
        ind = m
        break
      elif nums[m] > target:
        r = m - 1
      else:
        l = m + 1
    return ind