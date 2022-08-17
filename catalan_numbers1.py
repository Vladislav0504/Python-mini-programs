def Multiply_mod(a, b):
  lstb = []
  A = a
  while b != 1:
  	lstb.append(b)
  	b = b // 2
  lstb = lstb[::-1]
  for i in range(len(lstb)):
  	if lstb[i] % 2 == 0:
  	  a = a**2 % 1000000007
  	else:
  	  a = a**2 * A % 1000000007
  return a
def Catalan_mod(n):
  Clast, C = 1, 1
  for i in range(2,n + 1):
  	Clast, C = C, C * 2 * (2 * i - 1) * Multiply_mod(i + 1, 1000000005) % 1000000007
  return C
print(Catalan_mod(int(input())))