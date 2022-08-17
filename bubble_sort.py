class Solution:
  def bubbleSwapCount(self, A) -> int:
    k = 0
    for i in range(len(A)):
      for j in range(len(A) - i - 1):
        if A[j] > A[j + 1]:
          A[j], A[j + 1] = A[j + 1], A[j]
          k += 1
    return k