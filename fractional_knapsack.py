from sys import stdin


def main():
	n, W = map(int, input().split())
	R = [0] * n
	cost = 0
	for i, line in enumerate(stdin):
		c, w = map(int, line.split())
		R[i] = (c / w, w)
	R.sort()
	for c, w in R[::-1]:
		if W - w >= 0:
			cost += c * w
			W -= w
		elif W > 0:
			cost += W * c
			break
	print(cost)


if __name__ == '__main__':
	main()
