def longest_increasing_subsequence(n, A):
    D = [1] * n
    for i in range(n):
        for j in range(i):
            if A[i] % A[j] == 0 and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
    return max(D)


def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    print(longest_increasing_subsequence(n, A))


if __name__ == '__main__':
    main()
