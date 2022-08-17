from random import randint


def partition(l, r, A):
    x = A[l]
    j = l
    k = l
    for i in range(l + 1, r + 1):
        if A[i] < x:
            j += 1
            k += 1
            if i > k and k > j:
                A[j], A[i], A[k] = A[i], A[k], A[j]
            else:
                A[j], A[i] = A[i], A[j]
        elif A[i] == x:
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
            if m1 > l:
                quicksort(l, m1 - 1, A)
                l = m2 + 1
            else:
                l = m2 + 1
        else:
            if r > m2:
                quicksort(m2 + 1, r, A)
                r = m1 - 1
            else:
                r = m1 - 1


def main():
    n, m = map(int, input().split())
    A = [0] * n
    B = [0] * n
    for i in range(n):
        A[i], B[i] = map(int, input().split())
    P = [int(i) for i in input().split()]
    quicksort(0, n - 1, A)
    quicksort(0, n - 1, B)
    for j in range(m):
        c, c1 = 0, 0
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if A[m] <= P[j]:
                l = m + 1
                c = m + 1
            else:
                r = m - 1
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if B[m] >= P[j]:
                r = m - 1
            else:
                c1 = m + 1
                l = m + 1
        print(c - c1, end=' ')


if __name__ == '__main__':
    main()
