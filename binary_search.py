def main():
    A = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    lst = [-1] * b[0]
    for i in range(1, b[0] + 1):
        l, r = 1, A[0]
        while l <= r:
            m = (l + r) // 2
            if A[m] == b[i]:
                lst[i - 1] = m
                break
            elif A[m] > b[i]:
                r = m - 1
            else:
                l = m + 1
    print(*lst)


if __name__ == '__main__':
    main()
