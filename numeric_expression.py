def max_brackets(st):
    n = len(st) // 2 + 1
    D = [[0] * n for i in range(n)]
    for i in range(0, len(st), 2):
        D[i // 2][i // 2] = (int(st[i]),)
    actions = tuple(st[i] for i in range(1, len(st), 2))
    for j in range(1, n):
        for i in range(j, n):
            m, M = 10**30, -10**30
            for t in range(i - j, i):
                for num1 in D[i - j][t]:
                    for num2 in D[t + 1][i]:
                        res = eval(f'{num1}{actions[t]}{num2}')
                        m = min(m, res)
                        M = max(M, res)
            if m != M:
                D[i - j][i] = (m, M)
            else:
                D[i - j][i] = (m,)
    return max(D[0][n - 1])


def main():
    st = input()
    print(max_brackets(st))


if __name__ == '__main__':
    main()
