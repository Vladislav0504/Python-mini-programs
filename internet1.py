import requests
import re
A = input()
B = input()
res1 = requests.get(A)
k = 0
if res1.status_code == 200:
  lst1 = re.findall('<a href=\"(.+?)\">',res1.text)
  for elem1 in lst1:
  	res2 = requests.get(elem1)
  	if res2.status_code == 200:
  	  lst2 = re.findall('<a href=\"(.+?)\">',res2.text)
  	  if B in lst2:
  	  	print('Yes')
  	  	k = 1
  	  	break
if k == 0:
  print('No')