H = [1]
def Catalan_mod(n):
  global H
  if len(H) > n:
  	return H[n]
  else:
  	for i in range(len(H),n + 1):
  	  H.append(sum([Catalan_mod(k - 1) * Catalan_mod(i - k) for k in range(1, i + 1)]) % 1000000007)
  	return H[n]
print(Catalan_mod(int(input())))