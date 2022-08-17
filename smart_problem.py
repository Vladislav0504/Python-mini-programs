H = [int(i) for i in input().split()]
k = 0
M = max(H)
while M > 0:
  ind = 0
  for i in range(len(H)):
  	if H[i] == M:
  	  if i > 0:
  	  	H[i] = H[i - 1]
  	  else:
  	  	H[i] = 0
  	  if i == len(H) - 1:
  	  	k += 1
  	  if ind != 1:
  	   	ind = 1
  	elif ind == 1 and H[i] < M:
  	  k += 1
  	  ind = 0
  M = max(H)
print(k)