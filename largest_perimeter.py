class Solution:
  def largestPerimeter(self, A) -> int:
    for i in range(len(A)):
      for j in range(len(A) - i - 1):
        if A[j] > A[j + 1]:
          A[j], A[j + 1] = A[j + 1], A[j]
    B = [A[-1], A[-2], A[-3]]
    i = len(A) - 3
    while B[0] >= B[1] + B[2] and i >= 1:
      B[0], B[1], B[2] = B[1], B[2], A[i - 1]
      i -= 1
    if i == 0 and B[0] >= B[1] + B[2]:
      return 0
    return sum(B)