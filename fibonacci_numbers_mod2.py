def fib_mod(n, m):
    if n <= 1:
        return n
    res1, res2 = 0, 1
    p = 0
    for i in range(n - 1):
        res1, res2 = res2, (res2 + res1) % m
        if res1 == 0 and res2 == 1:
            p = i + 1
            break
    if p == 0:
        return res2
    w = n % p
    if w <= 1:
        return w
    for i in range(w - 1):
        res1, res2 = res2, (res2 + res1) % m
    return res2


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
