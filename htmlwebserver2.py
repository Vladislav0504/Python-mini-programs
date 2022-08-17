k = 10
print('<html>')
print('<body>')
print('<table>')
for j in range(1, k + 1):
  print('<tr>')
  for h in range(1, k + 1):
  	print('<td>',j * h,'</td>')
  print('</tr>')
print('</table>')
print('</body>')
print('</html>')