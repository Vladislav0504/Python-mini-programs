def IsPrime(n):
  d = 2
  while d * d <= n and n % d != 0:
  	d += 1
  return d * d > n
def primes():
  x = 1
  while True:
  	x += 1
  	while IsPrime(x) == False:
  	  x += 1
  	yield x