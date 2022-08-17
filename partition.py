class Solution:
  def partition(self, nums: list, P: int) -> list:
    for i in range(len(nums)):
      if nums[i] == P:
        nums[0], nums[i] = nums[i], nums[0]
    l, r = 0, len(nums) - 1
    x = P
    j, k = l, l
    for i in range(l + 1, r + 1):
      if nums[i] < x:
        j += 1
        k += 1
        if i > k and k > j:
          nums[j], nums[i], nums[k] = nums[i], nums[k], nums[j]
        else:
          nums[j], nums[i] = nums[i], nums[j] 
      elif nums[i] == x:
        k += 1
        nums[k], nums[i] = nums[i], nums[k]
    nums[l], nums[j] = nums[j], nums[l]
    return j + 1