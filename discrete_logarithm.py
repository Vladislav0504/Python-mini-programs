from math import sqrt, ceil, gcd

def factorize(n):
	i = 2
	p = []
	while i * i <= n:
		if n % i == 0:
			p.append(i)
			while n % i == 0:
				n = n // i
		if i > 2:
			i += 2
		else:
			i += 1
	if n > 1:
		p.append(n)
	return p

def euler_func(n):
	p = factorize(n)
	fi = n
	for el in p:
		fi -= fi // el
	return fi

def baby_steps_giant_steps(a, b, n):
	d = gcd(a, n)
	x = 0
	while d > 1:
		if b == 1:
			return x
		if b % d != 0:
			return -1
		n = n // d
		k = pow(a // d, -1, n)
		b = b // d * k % n
		x += 1
		d = gcd(a, n)
	if n == 1 or b == 1:
		return x

	m = ceil(sqrt(euler_func(n)))

	table = {}
	step = 1
	for k in range(m):
		table[step] = k
		step = step * a % n
	
	giant_stride = pow(a, -m, n)
	giant_step = b
	for i in range(m):
		if giant_step in table:
			return i * m + table[giant_step] + x
		giant_step = giant_step * giant_stride % n
	return -1

def main():
	a, b, n = map(int, input().split())
	print(baby_steps_giant_steps(a % n, b % n, n))
if __name__ == '__main__':
    main()