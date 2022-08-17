class Solution:
    def fastpw(self, n: int, m: int) -> int:
        if m == 0:
            return 1
        if m % 2 == 1:
            return n * self.fastpw(n, m - 1)
        else:
            return self.fastpw(n * n, m // 2)