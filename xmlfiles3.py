import xmltodict

fin = open('C:\\Users\\admin\\Downloads\\map2.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
count_fuel = 0
for some in parsedxml['osm']:
  for node in parsedxml['osm'][some]:
  	if 'tag' in node:
  	  tags = node['tag']
  	  if isinstance(tags, list):
  	    for tag in tags:
  	  	  if '@k' in tag and tag['@k'] == 'amenity' and tag['@v'] == 'fuel':
  	  	    count_fuel += 1
  	  elif isinstance(tags, dict):
  	    if '@k' in tags and tags['@k'] == 'amenity' and tags['@v'] == 'fuel':
  	  	  count_fuel += 1
print(count_fuel)