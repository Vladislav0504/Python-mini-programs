def Search(T):
	for i in enumerate(T):
		for j in enumerate(T[i[0]]):
			if j[1] == '0':
				return (i[0], j[0])
def Possibilities(i, j, T):
	global N, S, n
	Cannot = set()
	for k in range(N):
		if T[k][j] != '0':
		    Cannot.add(T[k][j])
		if T[i][k] != '0':
		    Cannot.add(T[i][k])
	for k in range(i - i % n, i - i % n + n):
		for t in range(j - j % n, j - j % n + n):
			if T[k][t] != '0':
				Cannot.add(T[k][t])
	return list(S.difference(Cannot))
def Solve(T):
	res = Search(T)
	if res is None:
		return True
	i, j = res[0], res[1]
	for el in Possibilities(i, j, T):
		T[i][j] = el
		if Solve(T):
			return True
		T[i][j] = '0'
N = 9
n = int(N**0.5)
S = set(str(i) for i in range(1, N + 1))
Table = [[] for j in range(N)]
for i in range(N):
	s = input()
	for j in range(N):
		Table[i].append(s[j])
Solve(Table)
for i in range(N):
	print(''.join(Table[i]))