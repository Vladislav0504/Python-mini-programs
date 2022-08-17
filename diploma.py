import math as m
w,h,n = map(int,input().split())
x = m.ceil(m.sqrt(n * w * h))
k = x // h
s = x // w
while k * s < n:
  t1 = w * (s + 1)
  t2 = h * (k + 1)
  if t1 < t2:
    s += 1
    x = t1
  else:
    k += 1
    x = t2
print(x)