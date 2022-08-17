from sys import stdin

def theorem(a, b, n, m):
	M = n * m
	s1 = pow(m, -1, n)
	s2 = pow(n, -1, m)
	return (a * s1 * m + b * s2 * n) % M

def main():
	N = int(input())
	for line in stdin:
		a, b, n, m = map(int, line.split())
		print(theorem(a, b, n, m))
if __name__ == '__main__':
    main()