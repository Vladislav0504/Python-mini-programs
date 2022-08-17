import xlrd

rb = xlrd.open_workbook('C:\\Users\\admin\\Downloads\\salaries.xlsx')
sheet = rb.sheet_by_index(0) #выбор активного листа

d1 = {}
d2 = {}
i = 1
for el in sheet.col_values(0)[1:]: #перебор элементов первого столбца со второй строки
  d1[el] = sheet.row_values(i)[1:]  #список элементов строки (i + 1)
  d1[el].sort()
  if len(d1[el]) % 2 == 1:
  	d1[el] = d1[el][len(d1[el]) // 2]
  else:
  	d1[el] = (d1[el][len(d1[el]) // 2] + d1[el][len(d1[el]) // 2 - 1]) / 2
  i += 1
M1 = 0
S1 = ''
for key in d1.keys():
  if d1[key] > M1:
  	M1 = d1[key]
  	S1 = key
i = 1
for el in sheet.row_values(0)[1:]: 
  d2[el] = sheet.col_values(i)[1:]
  d2[el] = sum(d2[el]) / len(d2[el])  
  i += 1
M2 = 0
S2 = ''
for key in d2.keys():
  if d2[key] > M2:
  	M2 = d2[key]
  	S2 = key
print(S1,S2)