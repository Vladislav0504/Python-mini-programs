import math
def f(x):
  return x**2 + math.sqrt(x)
def Res(C):
  a = 0
  b = C**2
  x = (a + b) / 2
  while abs(f(x) - C) > 10**(-6):
    if C < f(x):
      b = x
    else: 
      a = x
    x = (a + b) / 2
  return x
C = float(input())
x = Res(C)
print(x)