import xlrd

rb = xlrd.open_workbook('C:\\Users\\admin\\Downloads\\trekking1.xlsx')
sheet = rb.sheet_by_index(0) #выбор активного листа
lst = []
i = 1
for el in sheet.col_values(1)[1:]:
  lst.append([el,sheet.col_values(0)[i]])
  i += 1
lst.sort()
lst = lst[::-1]
Lst = []
K = 0
for el in lst:
  if el[0] != K:
  	Lst.sort()
  	for elem in Lst:
  	  print(elem)
  	Lst.clear()
  	Lst.append(el[1])
  	K = el[0]
  else:
  	Lst.append(el[1])
Lst.sort()
for el in Lst:
  print(el)
