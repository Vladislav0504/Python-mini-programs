class Solution:
  def sortArray(self, A):
    A1, A2 = [], []
    for i in range(len(A)):
      if A[i] % 2 == 0:
        A1.append(A[i])
      else:
        A2.append(A[i])
    for i in range(len(A1)):
      for j in range(len(A1) - i - 1):
        if A1[j] > A1[j + 1]:
          A1[j], A1[j + 1] = A1[j + 1], A1[j]
    for i in range(len(A2)):
      for j in range(len(A2) - i - 1):
        if A2[j] < A2[j + 1]:
          A2[j], A2[j + 1] = A2[j + 1], A2[j]
    for i in range(len(A)):
      if i % 2 == 0:
        A[i] = A1[i // 2]
      else:
        A[i] = A2[(i - 1) // 2]    
    return A