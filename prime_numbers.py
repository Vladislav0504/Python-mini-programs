class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        c, m = 1, n // 2
        lst = [1] * m
        for i in range(1, m):
            if lst[i]:
                c += 1
                h = 2 * i + 1
                for j in range(i, m, h):
                    lst[j] = 0
        return c