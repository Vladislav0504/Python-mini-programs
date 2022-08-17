def main():
	n = int(input())
	lst = []
	for k in range(1, n + 1):
		if n - k > k:
			lst.append(k)
			n -= k
		else:
			lst.append(n)
			break
	print(k)
	print(*lst)


if __name__ == '__main__':
	main()
