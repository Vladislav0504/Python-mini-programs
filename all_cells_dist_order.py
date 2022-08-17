class Solution:
  def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> list:
    A = [[[i, j] for j in range(C)] for i in range(R)]
    lst = []
    for i in range(R):
      for j in range(C):
        lst.append(A[i][j])
    for i in range(len(lst)):
      for j in range(len(lst) - i - 1):
        if (abs(r0 - lst[j][0]) + abs(c0 - lst[j][1])) > (abs(r0 - lst[j + 1][0]) + abs(c0 - lst[j + 1][1])):
          lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst