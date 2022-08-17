def z(s):
    L, R = 1, 1
    z = [0] * (len(s) + 1)
    for i in range(2, len(s) + 1):
        z[i] = 0
        if i < R:
            z[i] = min(z[i - L + 1], R - i)
        while i + z[i] <= len(s) and s[z[i]] == s[z[i] + i - 1]:
            z[i] += 1
        if i + z[i] > R:
            L = i
            R = i + z[i]
    return z[2:]
s = input()
print(*z(s))