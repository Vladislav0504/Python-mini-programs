import random as rm
s = input()
l, r = 1, 10
ind = 0
while l < r:
    m = rm.randint(l, r)
    try:
        if type(s[m - 1]) is str:
            l = m
    except IndexError:
        ind = 1
        r = m - 1
    if l == r and ind == 0:
        r *= 2
print(l)