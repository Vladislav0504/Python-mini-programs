def longest_increasing_subsequence(n, A):
    D = [-1] * (n + 1)
    D[0] = 10**9
    prev = [-1] * n
    indexes = [0] * n
    k, ind = 0, 0
    for j in range(n):
        l, r = 0, n
        while l <= r:
            m = (l + r) // 2
            if D[m] >= A[j]:
                l = m + 1
            else:
                r = m - 1
        if A[j] > D[r + 1]:
            D[r + 1] = A[j]
            indexes[r] = j
            if j > 0 and r > 0:
                prev[j] = indexes[r - 1]
        if r + 1 > k:
            k = r + 1
            ind = j
    print(k)
    L = [ind + 1]
    while prev[ind] != -1:
        ind = prev[ind]
        L.append(ind + 1)
    return L[::-1]


def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    print(*longest_increasing_subsequence(n, A))


if __name__ == '__main__':
    main()
