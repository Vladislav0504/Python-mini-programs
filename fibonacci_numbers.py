def fib(n):
	if n <= 1:
		return n
	res1, res2 = 0, 1
	for i in range(n - 1):
		res1, res2 = res2, res2 + res1
	return res2


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
