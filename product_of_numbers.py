# Для ускорения можно считать полиномы по основанию не 10, а 100, 1000, 10000 и т.д.
from math import log2, ceil, pi
import cmath

def bit_reverse_copy(a, n, K):
	return [a[A[i]] for i in range(n)]

def bit_reverse_copy1(a, b, n, K):
	global A
	A = [0] * n
	d = T[K - 1]
	for b1 in T[:K]:
		for i in range(b1):
			A[i + b1] = A[i] + d
		d = d // 2
	return [a[A[i]] for i in range(n)], [b[A[i]] for i in range(n)]

def fft1(a, b, n, w, K):
	a, b = bit_reverse_copy1(a, b, n, K)
	d = n // 2
	for b1 in T[:K]:
		h = d // b1
		for i in range(0, n, 2 * b1):
			s = 0
			for k in range(i, b1 + i):
				t = b1 + k
				c = w[s]
				ela, elb = a[k], b[k]
				pa, pb = a[t] * c, b[t] * c
				a[k], a[t] = ela + pa, ela - pa
				b[k], b[t] = elb + pb, elb - pb
				s += h
	return a, b

def fft(a, n, w, K):
	a = bit_reverse_copy(a, n, K)
	d = n // 2
	for b in T[:K]:
		h = d // b
		for i in range(0, n, 2 * b):
			s = 0
			for k in range(i, b + i):
				t = b + k
				el = a[k]
				p = a[t] * w[s]
				a[k], a[t] = el + p, el - p
				s += h
	return a

def fft_inverse(g, n, w, K):
	b = fft(g, n, w, K)
	h = round(b[0].real / n)
	for i in range(n - 1, -1, -1):
		h1 = round(b[i].real / n)
		b[i] = str(h % 10)
		h = h // 10
		h += h1
	if s < 0:
		ans = '-'
		j = 1
	else:
		ans = ''
		j = 0
	for el in b:
		if len(ans) > j or el != '0':
			ans += el
	return ans

def main():
	a = input()
	b = input()

	if a == '0' or b == '0':
		print(0)
	else:
		global T, s
		la, lb = len(a), len(b)
		if a[0] == '-':
			s, length = -1, la - 1
		else:
			s, length = 1, la
		if b[0] == '-':
			s = -s
			if lb - 1 > length:
				length = lb - 1
		elif lb > length:
			length = lb
		k = ceil(log2(length)) + 1
		T = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]
		n = T[k]

		A = [int(a[i]) if i >= 0 and a[i] != '-' else 0 for i in range(la - 1, la - 1 - n, -1)]
		B = [int(b[i]) if i >= 0 and b[i] != '-' else 0 for i in range(lb - 1, lb - 1 - n, -1)]

		w = [1] * T[k - 1]
		h = cmath.rect(1, 2 * pi / n)
		for i in range(1, T[k - 1]):
			w[i] = w[i - 1] * h

		u, v = fft1(A, B, n, w, k)
	
		g = [u[i] * v[i] for i in range(n)]
	
		print(fft_inverse(g, n, w, k))
if __name__ == '__main__':
   main()