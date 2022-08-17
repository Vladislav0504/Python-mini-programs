def prefix(s):
    p = [0] * len(s)
    k = 0
    for i in range(1, len(s)):
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p
s = input()
t = len(s) - prefix(s)[-1]
if len(s) % t != 0:
    t = len(s)
print(t)