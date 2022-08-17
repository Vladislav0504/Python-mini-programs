import xlrd
import urllib.request
import zipfile as z
import os

urllib.request.urlretrieve('https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip', 'C:\\Users\\admin\\Downloads\\rubbish\\rogaikopyta.zip')
Zip = z.ZipFile('C:\\Users\\admin\\Downloads\\rubbish\\rogaikopyta.zip')
Zip.extractall('C:\\Users\\admin\\Downloads\\rubbish')
os.chdir('C:\\Users\\admin\\Downloads\\rubbish')
d = ['' for i in range(1,1001)]
for i in range(1000):
  rb = xlrd.open_workbook('C:\\Users\\admin\\Downloads\\rubbish\\%d.xlsx' % (i + 1))
  sheet = rb.sheet_by_index(0)
  d[i] = [sheet.row_values(1)[1], sheet.row_values(1)[3]]
d.sort()
for el in d:
  print(el[0],int(el[1]))