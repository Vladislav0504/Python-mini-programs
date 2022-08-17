def edit_dist(A, B):
    n = len(A)
    m = len(B)
    D = [[i for j in range(m + 1)] for i in range(n + 1)]
    for j in range(1, m + 1):
        D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + (A[i - 1] != B[j - 1]))
    return D[n][m]


def main():
    A = input()
    B = input()
    print(edit_dist(A, B))


if __name__ == '__main__':
    main()
