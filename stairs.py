def stairs(n, A):
	d0, d1 = 0, A[0]
	for i in range(2, n + 1):
		d0, d1 = d1, max(d1, d0) + A[i - 1]
	return d1


def main():
	n = int(input())
	A = [int(a) for a in input().split()]
	print(stairs(n, A))


if __name__ == '__main__':
    main()
