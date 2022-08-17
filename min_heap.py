def build_heap(A):
    for i in range((len(A) - 1) // 2, -1, -1):
        sift_down(A, i)


def sift_down(A, i):
    global swaps
    while 2 * i + 1 < len(A):
        j = 2 * i + 1
        k = j + 1
        if k < len(A) and A[j] > A[k]:
            j = k
        if A[i] <= A[j]:
            break
        A[i], A[j] = A[j], A[i]
        swaps.append((i, j))
        i = j

        
def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    build_heap(A)
    print(len(swaps))
    for swap in swaps:
        print(*swap)


if __name__ == '__main__':
    swaps = []
    main()
