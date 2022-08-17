def countsort(n, A):
    B = [0] * 10
    for j in range(n):
        B[A[j] - 1] += 1
    for i in range(1, 10):
        B[i] += B[i - 1]
    A1 = [0] * n
    for j in range(n - 1, -1, -1):
        B[A[j] - 1] -= 1
        A1[B[A[j] - 1]] = A[j]
    return A1


def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    print(*countsort(n, A))


if __name__ == '__main__':
    main()
