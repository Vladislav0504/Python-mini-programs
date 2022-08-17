import sys

sys.setrecursionlimit(100000)


def pre_order(v, left, right):
    global T, res
    if v[0] >= right or v[0] <= left:
        res = 'INCORRECT'
    else:
        if v[1] != -1:
            pre_order(T[v[1]], left, v[0])
        if v[2] != -1:
            pre_order(T[v[2]], v[0], right)


def main():
    for i, line in enumerate(sys.stdin):
        key, left, right = map(int, line.split())
        T[i] = (key, left, right)
    if T:
        pre_order(T[0], -2**31, 2**31 - 1)
    print(res)


if __name__ == '__main__':
    n = int(input())
    res = 'CORRECT'
    T = [0] * n
    main()
