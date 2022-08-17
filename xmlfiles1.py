import xmltodict

fin = open('C:\\Users\\admin\\Downloads\\map1.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
count_tag = 0
count_without_tag = 0
for node in parsedxml['osm']['node']:
  if 'tag' in node:
  	count_tag += 1
  else:
  	count_without_tag += 1
print(count_tag, count_without_tag)