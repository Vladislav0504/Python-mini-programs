from sys import stdin


def in_order(v, T):
    if v[1] != -1:
        in_order(T[v[1]], T)
    print(v[0], end=' ')
    if v[2] != -1:
        in_order(T[v[2]], T)


def pre_order(v, T):
    print(v[0], end=' ')
    if v[1] != -1:
        pre_order(T[v[1]], T)
    if v[2] != -1:
        pre_order(T[v[2]], T)


def post_order(v, T):
    if v[1] != -1:
        post_order(T[v[1]], T)
    if v[2] != -1:
        post_order(T[v[2]], T)
    print(v[0], end=' ')


def main():
    n = int(input())
    T = [0] * n
    for i, line in enumerate(stdin):
        key, left, right = map(int, line.split())
        T[i] = (key, left, right)
    in_order(T[0], T)
    print()
    pre_order(T[0], T)
    print()
    post_order(T[0], T)


if __name__ == '__main__':
    main()
