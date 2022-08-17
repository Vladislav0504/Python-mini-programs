class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        k, p = 0, 1
        while k < n:
            k += p
            p += 2
        if k == n:
            return True
        return False