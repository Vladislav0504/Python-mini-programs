with open('F:\\dataset_3363_2.txt','r') as f:
  s1 = f.readline()
s = ''
sc = '0'
i = 0
t = ''
s1 +=' '
integer = ['0','1','2','3','4','5','6','7','8','9']
while i < len(s1):
  if s1[i] not in integer:
    t = s1[i]
    i += 1
  else:
    while s1[i] in integer:
      sc += s1[i]
      i += 1
  sc = int(sc)
  s += t * sc
  sc = '0'
with open('F:\\text2.txt','w') as f2:
  f2.write(s)