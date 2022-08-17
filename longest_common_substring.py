from itertools import zip_longest, islice
# itertools.islice(iterable, [start], stop[, step]) - итератор, состоящий из среза
# itertools.zip_longest(*iterables, fillvalue=None) - как zip, но берет самый длинный итератор, а более короткие дополняет fillvalue
# (zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-)

def get_classes(st):
    chars = set(st)
    lst = list(chars)
    lst.sort()
    M = len(lst) - 1
    index = {v: i for i, v in enumerate(lst)}
    return [index[v] for v in st], M

def suffix_array(st):
    n = len(st)
    k = 1
    c, M = get_classes(st)
    while M < n - 1:
        c, M = get_classes(
            [a * (n + 1) + b + 1 for (a, b) in zip_longest(c, islice(c, k, None), fillvalue=-1)])
        k <<= 1 # бинарный сдвиг, увеличение k в 2 раза
    return c

def inverse_array(p):
    n = len(p)
    ans = [0] * n
    for i in range(n):
        ans[p[i]] = i
    return ans

def lcp(s, p, p1):
    n = len(s)
    s = s + '$' + s
    k = 0
    d = [0] * n
    for i in range(n):
        k = max(k - 1, 0)
        pos = p1[i]
        if pos + 1 < n:
            j = p[pos + 1]
            while s[i + k] == s[j + k]:
                k += 1
            d[pos] = k
    return d[:n - 1]
s = input()
t = input()
if len(s) <= len(t):
    st = s + '#' + t
    dic = [0 if i < len(s) else 1 if i > len(s) and i < len(st) else -1 for i in range(len(st))]
else:
    st = t + '#' + s
    dic = [1 if i < len(t) else 0 if i > len(t) and i < len(st) else -1 for i in range(len(st))]
lst = suffix_array(st)
suffix = inverse_array(lst)
numbers = [dic[el] for el in suffix]
M = [0, -1]
my_lcp = lcp(st, suffix, lst)
for i, elem in enumerate(my_lcp):
    if numbers[i] != -1 and numbers[i] != numbers[i + 1] and M[0] < elem:
        M = [elem, suffix[i]]
print(st[M[1]:M[1] + M[0]])