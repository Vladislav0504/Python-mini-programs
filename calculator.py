def calculator(n):
    K = [i for i in range(-1, n)]
    prev = [1] * (n + 1)
    for i in range(1, n):
        for j in (i + 1, i * 2, i * 3):
            if j <= n and K[j] > K[i] + 1:
                K[j] = K[i] + 1
                prev[j] = i
    print(K[n])
    lst = [n] * (K[n] + 1)
    for j in range(K[n], 0, -1):
        lst[j - 1] = prev[lst[j]]
    return lst


def main():
    n = int(input())
    print(*calculator(n))


if __name__ == '__main__':
    main()
