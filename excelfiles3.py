import xlrd
import math as m

rb = xlrd.open_workbook('C:\\Users\\admin\\Downloads\\trekking2.xlsx')
sheet1 = rb.sheet_by_index(0)
sheet2 = rb.sheet_by_index(1)
Calories, protein, fat, carbohydrates = 0, 0, 0, 0
d1 = {}
for i in range(1,len(sheet2.col_values(0))):
  d1[sheet2.row_values(i)[0]] = d1.get(sheet2.row_values(i)[0],0) + sheet2.row_values(i)[1]
d2 = {}
for i in range(1,len(sheet1.col_values(0))):
  d2[sheet1.row_values(i)[0]] = [sheet1.row_values(i)[1], sheet1.row_values(i)[2], sheet1.row_values(i)[3], sheet1.row_values(i)[4]]
for key in d1.keys():
  Calories += d2[key][0] * d1[key] / 100 if type(d2[key][0]) is float else 0
  protein += d2[key][1] * d1[key] / 100 if type(d2[key][1]) is float else 0
  fat += d2[key][2] * d1[key] / 100 if type(d2[key][2]) is float else 0
  carbohydrates += d2[key][3] * d1[key] / 100 if type(d2[key][3]) is float else 0
print(m.floor(Calories), m.floor(protein), m.floor(fat), m.floor(carbohydrates))