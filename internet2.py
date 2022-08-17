import requests
import re
A = input()
lst = []
res = requests.get(A)
url_lst = re.findall('<a.+href?=[\",\'](.+?[\",\']).*>?',res.text)
for elem in url_lst:
  x = ''
  i = 0
  while i < len(elem):
    if elem[i] == ':' and elem[i + 1] == '/' and elem[i + 2] == '/':
      x = ''
      i += 3
    elif elem[i] == '.' and elem[i + 1] == '.' and elem[i + 2] == '/':
      x = ''
      break
    elif re.search('[\w,\.,\-]',elem[i]) == None:
      break
    else:
      x += elem[i]
      i += 1
  if len(x) > 0 and x not in lst:
  	lst.append(x)
lst.sort()
for elem in lst:
  print(elem)