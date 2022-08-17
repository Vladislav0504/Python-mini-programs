class Solution:
    def countSubstrings(self, s: str) -> int: # алгоритм Манакера
        S = 0
        n = len(s)
        d1, d2 = [1] * n, [0] * n
        l1, l2, r1, r2 = 0, 0, -1, -1
        for i in range(n):
            if i <= r1:
                d1[i] = min(d1[l1 + r1 - i], r1 - i + 1)
            while i + d1[i] < n and i - d1[i] >= 0 and s[i + d1[i]] == s[i - d1[i]]:
                d1[i] += 1
            if i + d1[i] - 1 > r1:
                r1 = i + d1[i] - 1
                l1 = i - d1[i] + 1
            if i <= r2:
                d2[i] = min(d2[l2 + r2 - i + 1], r2 - i + 1)
            while i + d2[i] < n and i - d2[i] - 1 >= 0 and s[i + d2[i]] == s[i - d2[i] - 1]:
                d2[i] += 1
            if i + d2[i] - 1 > r2:
                r2 = i + d2[i] - 1
                l2 = i - d2[i]
            S += d1[i] + d2[i]
        return S
