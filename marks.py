a = []
d = [0,0,0,0]
with open('F:\\dataset_3363_4.txt','r', encoding='utf-8') as f:
  for l in f:
    l = [j for j in l.split(';')]
    for i in range(3):
      l[i + 1] = int(l[i + 1])
      d[i] += l[i + 1]
    a.append((l[1] + l[2] + l[3]) / 3)
    d[3] += 1
a1 = d[0] / d[3]
a2 = d[1] / d[3]
a3 = d[2] / d[3]
with open('F:\\text.txt','w') as f1:
  for i in range(d[3]):
    f1.write(str(a[i])+'\n')
  f1.write(str(a1)+' '+str(a2)+' '+str(a3))