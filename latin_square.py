import random as rm
n, h = 26, 2
Rows = [chr(i) for i in range(65, 65 + n)]
Table = [[0 for i in range(n)] for j in range(n)]
rm.shuffle(Rows)
while n % h == 0:
	h = rm.randint(1, n - 1)
Table[0] = Rows
for i in range(1, n):
	for j in range(n):
		Table[i][j] = Rows[(j + i * h) % n]
S = [i for i in range(n)]
rm.shuffle(S)
rm.shuffle(Table)
for i in range(n):
	print(''.join([Table[i][j] for j in S]))