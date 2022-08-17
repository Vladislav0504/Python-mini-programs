from sys import stdin
from random import randint

def sort_letters(s):
    global classes
    n = len(s)
    for i in range(n):
        cnt[ord(s[i]) - 32] += 1
    for i in range(1, 96):
        cnt[i] += cnt[i - 1]
    for i in range(n):
        cnt[ord(s[i]) - 32] -= 1
        p[cnt[ord(s[i]) - 32]] = i
        p1[i] = cnt[ord(s[i]) - 32]
    c[0] = 0
    classes = 1
    for i in range(1, n):
        if s[p[i]] != s[p[i - 1]]:
            classes += 1
        c[i] = classes - 1

def digit_sort(a):
    global classes
    n = len(a)
    a1 = [0] * n
    for j in range(1, -1, -1):
        cnt = [0] * classes
        cnt2 = [0] * classes
        for i in range(n):
            cnt[a[i][j]] += 1
        for i in range(1, classes):
            cnt2[i] = cnt2[i - 1] + cnt[i - 1]
        for i in range(n):
            a1[cnt2[a[i][j]]] = a[i]
            cnt2[a[i][j]] += 1
        for i, el in enumerate(a1):
            a[i] = el

def suffix_array(s):
    global classes, p, p1
    n = len(s)
    a = [0] * n
    k = 0
    while (1 << k) < n and classes < n:
        for i in range(n):
            a[i] = (c[p1[i]], c[p1[(i + (1 << k)) % n]], i)
        digit_sort(a)
        c[0] = 0
        an = (a[0][0], a[0][1])
        p1[a[0][2]] = 0
        for i in range(1, n):
            if an != (a[i][0], a[i][1]):
                c[i] = c[i - 1] + 1
                an = (a[i][0], a[i][1])
            else:
                c[i] = c[i - 1]
            p1[a[i][2]] = i
        classes = c[-1] + 1
        k += 1
    if a[0] != 0:
        p = [el[2] for el in a]

def rmq_sparse_table(L, R):
    global h, f
    t = h[R - L - 1]
    return min(f[L][t], f[R - (1 << t)][t])

def calc_sparse_table(a, n):
    global h, f
    h = [0] * n
    for i in range(1, n):
        h[i] = h[(i + 1) // 2 - 1] + 1
    f = [[-1 for j in range(h[n - 1] + 1)] for i in range(n)]
    for i in range(n):
        f[i][0] = a[i]
    for k in range(1, h[n - 1] + 1):
        for i in range(n):
            f[i][k] = f[i][k - 1]
            p = i + (1 << (k - 1))
            if p < n and f[p][k - 1] < f[i][k]:
                f[i][k] = f[p][k - 1]

def compare(li, ri, lx, rx, A, i, x):
    ind = -1
    if li == lx:
        if lens[A[i]] == lens[x]:
            ind = 1
        elif lens[A[i]] < lens[x]:
            ind = 0
    else:
        if p1[li - 1] < p1[lx - 1]:
            our_lcp = rmq_sparse_table(p1[li - 1], p1[lx - 1])
        else:
            our_lcp = rmq_sparse_table(p1[lx - 1], p1[li - 1])
        length = min(our_lcp, lens[A[i]], lens[x])
        if length == lens[A[i]] == lens[x]:
            if li < lx:
                ind = 0
        elif length == lens[A[i]] or length < lens[A[i]] and length != lens[x] and s[li - 1 + length] < s[lx - 1 + length]:
            ind = 0
    return ind

def partition(l, r, A):
    x = A[l]
    j = l
    k = l
    for i in range(l + 1, r + 1):
        li, ri = substrings[A[i]]
        lx, rx = substrings[x]
        ind = compare(li, ri, lx, rx, A, i, x)
        if ind == 0:
            j += 1
            k += 1
            if i > k and k > j:
                A[j], A[i], A[k] = A[i], A[k], A[j]
            else:
                A[j], A[i] = A[i], A[j]
        elif ind == 1:
            k += 1
            A[k], A[i] = A[i], A[k]
    A[l], A[j] = A[j], A[l]
    return j, k

def quicksort(l, r, A):
    while l < r:
        rand = randint(l, r)
        A[l], A[rand] = A[rand], A[l]
        m1, m2 = partition(l, r, A)
        if m1 - l <= r - m2:
            quicksort(l, m1 - 1, A)
            l = m2 + 1
        else:
            quicksort(m2 + 1, r, A)
            r = m1 - 1

def inverse_array(p):
    n = len(p)
    ans = [0] * n
    for i in range(n):
        ans[p[i]] = i
    return ans

def lcp(s, p, p1):
    n = len(s)
    s = s + ' ' + s
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

def main():
    global s, p1, p, substrings, lens, c, cnt
    cnt = [0] * 96
    s = input()
    p = [0] * (len(s) + 1)
    p1 = [0] * (len(s) + 1)
    c = [0] * (len(s) + 1)
    n = int(input())
    sort_letters(s + ' ')
    suffix_array(s + ' ')
    p1 = inverse_array(p[1:])
    my_lcp = lcp(s, p[1:], p1)
    if n > 1:
        calc_sparse_table(my_lcp, len(s) - 1)
    substrings = [0] * n
    lens = [1] * n
    A = [i for i in range(n)]
    for i, line in enumerate(stdin):
        l, r = map(int, line.split())
        substrings[i] = (l, r)
        lens[i] = r - l + 1
    quicksort(0, n - 1, A)
    for el in A:
        print(*substrings[el])
if __name__ == '__main__':
    main()
