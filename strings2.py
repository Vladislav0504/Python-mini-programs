s = input()
t = input()
k, i = 0, 0
while s.find(t, i, len(s)) != -1:
  k += 1
  i = s.find(t, i, len(s)) + 1
print(k)