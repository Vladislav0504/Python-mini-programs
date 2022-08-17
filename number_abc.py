def Number_abc(s):
  l = len(s)
  f = [[0 for i in range(l)] for j in range(3)]
  for i in range(l):
    if i >= 1:
      f[0][i] = f[0][i - 1]
      f[1][i] = f[1][i - 1]
      f[2][i] = f[2][i - 1]
    if s[i] == 'a':
      f[0][i] += 1
    elif s[i] == 'b' and i >= 1:
      f[1][i] += f[0][i - 1]
    elif s[i] == 'c' and i >= 2:
      f[2][i] += f[1][i - 1]
  return f[2][l - 1]
s = str(input())
C = Number_abc(s)
print(C)