class Solution:
  def nextGreatestLetter(self, letters, target: str) -> str:
    l, r = 0, len(letters) - 1
    while l <= r:
      m = (l + r) // 2
      if letters[m] <= target:
        if m == len(letters) - 1:
          return letters[0]
        l = m + 1
      elif letters[m] > target:
        r = m - 1
    return letters[r + 1]