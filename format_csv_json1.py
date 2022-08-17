import pandas as pd
import os
os.chdir("C:/Users/admin/Downloads/")
df = pd.read_csv('Crimes.csv', sep=",")
df2 = pd.DataFrame({
	'Date': df['Date'].astype(str),
	'Primary Type': df['Primary Type']
	})
Type = {}
for i in range(len(df2)):
  if df2['Date'][i][8] == '1' and df2['Date'][i][9] == '5':
  	if df2['Primary Type'][i] not in Type.keys():
  	  Type[df2['Primary Type'][i]] = 1
  	else:
  	  Type[df2['Primary Type'][i]] += 1
Max = ''
k = 0
for elem in Type.keys():
  if Type[elem] > k:
  	k, Max = Type[elem], elem
print(Max)