from urllib.request import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
s = str(html)
d = {}
k1, k2 = 0, 0
lst = []
M = 0
while s:
  k1 = s.find('<code>', k2)
  k2 = s.find('</code>', k1)
  if k1 == -1:
  	break
  text = ''.join([s[i] for i in range(k1 + 6,k2)])
  d[text] = d.get(text,0) + 1
for key in d.keys():
  if d[key] > M:
  	lst.clear()
  	lst.append(key)
  	M = d[key]
  elif d[key] == M:
  	lst.append(key)
lst.sort()
for el in lst:
  print(el,end=' ')