class Solution:
    def minSteps(self, s: str, t: str) -> int: # шагов до получения из t анаграммы s
        sdict = {}
        ans = 0
        for elem in s:
            sdict[elem] = sdict.get(elem, 0) + 1
        for elem in t:
            if elem in sdict.keys() and sdict[elem] > 0:
                sdict[elem] -= 1
            else:
                ans += 1
        return ans