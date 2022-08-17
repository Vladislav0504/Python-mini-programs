T = []
class Solution:
    def combinationSum(self, nums: list, target: int, lst = []) -> list:
        global T
        nums.sort()
        s = [tuple(lst) for i in range(len(nums))]
        for i, elem in enumerate(nums):
            D = target
            D -= elem
            if D >= elem:
                self.combinationSum(nums[i + 1:], D, list(s[i]) + [elem])
            elif D == 0:
                T.append(list(s[i]) + [elem])
        for i in range(len(T)):
            for j in range(i + 1, len(T)):
                if T[i] == T[j]:
                    T.pop(j)
        return T