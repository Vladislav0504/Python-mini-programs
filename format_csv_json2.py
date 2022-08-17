import json
data = json.loads(input())
d = {}
for i in range(len(data)):
  d[data[i]['name']] = data[i]['parents']
  if data[i]['name'] not in data[i]['parents']:
  	d[data[i]['name']].append(data[i]['name'])
for key in d.keys():
  for elem in d[key]:
  	if elem not in d.keys():
  	  d[elem] = [elem]
for key in d.keys():
  for elem in d[key]:
  	for el in d[elem]:
  	  if el not in d[key]:
  	  	d[key].append(el)
d1 = {}
lst = list(d.keys())
lst.sort()
for elem in lst:
  d1[elem] = 0
  for el in lst:
  	if elem in d[el]:
  	  d1[elem] += 1
  print(elem,':',d1[elem])