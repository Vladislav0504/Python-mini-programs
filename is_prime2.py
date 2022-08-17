from sys import stdin
from random import randint

def miller_rabin(n, t):
	if n <= 1:
		return 'NO'
	if n == 2 or n == 3:
		return 'YES'
	if n % 2 == 0:
		return 'NO'
	s = n - 1
	k = 0
	while s % 2 == 0:
		s = s // 2
		k += 1
	for i in range(1, t + 1):
		x = randint(2, n - 2)
		if not check(n, x, s, k):
			return 'NO'
	return 'YES'

def check(n, x, s, k):
	y = pow(x, s, n)
	if y == 1 or y == n - 1:
		return True
	for j in range(1, k):
		y = y * y % n
		if y == 1:
			return False
		if y == n - 1:
			return True
	return False

def main():
	n = int(input())
	for line in stdin:
		q = int(line)
		print(miller_rabin(q, 3))
if __name__ == '__main__':
    main()