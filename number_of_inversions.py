def merge(A, B):
    global c
    D = []
    Ai, Bi = 0, 0
    while Ai < len(A) and Bi < len(B):
        if A[Ai] <= B[Bi]:
            D.append(A[Ai])
            Ai += 1
        else:
            D.append(B[Bi])
            c += len(A) - Ai
            Bi += 1
    D.extend(A[Ai:])
    D.extend(B[Bi:])
    return D


def mergesort(l, r, A):
    if l < r:
        m = (l + r) // 2
        return merge(mergesort(l, m, A), mergesort(m + 1, r, A))
    return [A[l]]


def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    mergesort(0, n - 1, A)
    print(c)


if __name__ == '__main__':
    c = 0
    main()
