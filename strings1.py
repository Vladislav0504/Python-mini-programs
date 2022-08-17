s = input()
a = input()
b = input()
k = 0
while k <= 1001 and a in s:
  s = s.replace(a,b)
  k += 1
if k <= 1000:
  print(k)
else: 
  print('Impossible')