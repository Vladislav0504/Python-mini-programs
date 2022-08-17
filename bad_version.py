class Solution:
  def firstBadVersion(self, n: int) -> int:
    l, r = 1, n + 1
    while l < r:
      m = (l + r) // 2
      if isBadVersion(m):
        if not isBadVersion(m - 1):
          return m
        else:
          r = m
      else:
        l = m + 1