i = 1
k = 2
print('<html>')
print('<body>')
print('<table>')
for j in range(k):
  print('<tr>')
  for h in range(k):
  	print('<td>',i,'</td>')
  	i += 1
  print('</tr>')
print('</table>')
print('</body>')
print('</html>')