from sys import stdin


def main():
    st = input()
    q = int(input())
    for line in stdin:
    	i, j, k  = map(int, line.split())
    	ends = st[: i] + st[j + 1 :]
    	st = ends[: k] + st[i : j + 1] + ends[k :]
    print(st)


if __name__ == '__main__':
    main()
