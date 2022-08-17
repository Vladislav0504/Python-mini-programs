d = dict()
with open('F:\\dataset_3380_5.txt','r') as f:
  for line in f:
    line = [j for j in line.split()]
    line[0] = int(line[0])
    line[2] = float(line[2])
    if line[0] not in d:
      d[line[0]] = [line[2],1]
    else:
      d[line[0]][1] += 1
      d[line[0]][0] += line[2]
a = []
for i in range(1,12):
  if i in d:
    a.append(d[i][0] / d[i][1])
  else:
    a.append('-')
with open('F:\\text.txt','w') as f1:
  for i in range(11):
    f1.write(str(i + 1)+' '+str(a[i])+'\n')