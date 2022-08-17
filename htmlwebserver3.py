k = 10
print('<html>')
print('<body>')
print('<table>')
for j in range(1, k + 1):
  print('<tr>')
  for h in range(1, k + 1):
  	print('<td> <a href=http://' + str(j * h) + '.ru>' + str(j * h) + '</a> </td>')
  print('</tr>')
print('</table>')
print('</body>')
print('</html>')