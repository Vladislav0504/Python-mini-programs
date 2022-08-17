from sys import stdin


def main():
	n = int(input())
	R = [0] * n
	for i, line in enumerate(stdin):
		l, r = map(int, line.split())
		R[i] = (r, l)
	R.sort()
	lst = [R[0][0]]
	for el in R:
		if el[1] > lst[-1]:
			lst.append(el[0])
	print(len(lst))
	print(*lst)


if __name__ == '__main__':
	main()
