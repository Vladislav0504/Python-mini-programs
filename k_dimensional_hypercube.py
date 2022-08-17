import sys
def main():
  with open('C:\\Users\\admin\\Downloads\\cube.txt', 'r') as f:
  	for line in f:#sys.stdin:
  	  A, B = line.split()
  k = len(A)
  cycle1 = []
  cycle2 = []
  for i in range(k):
    if A[i] != B[i]:
      cycle1.append(i)
    else:
      cycle2.append(i)
  lst = [[A] for j in range(k)]
  l1 = len(cycle1)
  for i in range(l1):
  	for j in range(l1):
  	  s = lst[j][-1]
  	  numb = cycle1[(i + j) % l1] % k
  	  lst[j].append(s[:numb] + str((int(s[numb]) + 1) % 2) + s[numb + 1:])
  for j in range(l1, k):
  	s = lst[j][-1]
  	numb = cycle2[j - l1] % k
  	lst[j].append(s[:numb] + str((int(s[numb]) + 1) % 2) + s[numb + 1:])
  for i in range(l1):
  	for j in range(l1, k):
  	  s = lst[j][-1]
  	  numb = cycle1[(i + j - l1) % l1] % k
  	  lst[j].append(s[:numb] + str((int(s[numb]) + 1) % 2) + s[numb + 1:])
  for j in range(l1, k):
  	lst[j].append(B)
  for el in lst:
  	print(*el)
if __name__ == '__main__':
  main()