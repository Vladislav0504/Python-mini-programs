class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        p, substr = 0, ''
        struct = list(zip(*strs)) # список кортежей min длины слова в strs, состоящих из соответствующих букв слов в strs
        min_length = len(struct)
        while p < min_length and len(set(struct[p])) == 1: # пока набор кортежа состоит из одной буквы, идем к следующему кортежу
            p, substr = p + 1, substr + strs[0][p]
        return substr