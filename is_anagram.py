class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    As = [s[i] for i in range(len(s))]
    At = [t[i] for i in range(len(t))]
    for i in range(len(s)):
      for j in range(len(s) - i - 1):
        if As[j] > As[j + 1]:
          As[j], As[j + 1] = As[j + 1], As[j]
    for i in range(len(t)):
      for j in range(len(t) - i - 1):
        if At[j] > At[j + 1]:
          At[j], At[j + 1] = At[j + 1], At[j]
    if As != At:
      return False
    return True