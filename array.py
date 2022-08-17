A = [int(i) for i in input().split()]
B = [-1 for i in range(len(A))]
for i in range(len(A)):
  for j in range(i + 1, len(A)):
  	if A[j] > A[i]:
  	  B[i] = A[j]
  	  break
print(*B)