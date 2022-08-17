d = dict()
with open('F:\\dataset_3363_3.txt','r') as f:
  for line in f:
    line = line.strip().lower()
    line = [j for j in line.split()]
    for elem in line:
      if elem in d:
        d[elem] += 1
      else:
        d[elem] = 1      
key = line[0]
value = d[line[0]]
for elem in d:
  if (d[elem] > value) or (d[elem] == value) and (key >= elem):
    value = d[elem]
    key = elem
with open('F:\\text.txt','w') as f1:
  f1.write(key+' '+str(value))