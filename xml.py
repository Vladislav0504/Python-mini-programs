from xml.etree import ElementTree
def Prices(root):
  global Price
  Price[root.attrib['color']] += root.attrib['price']
  for child in root:
  	child.attrib['price'] = root.attrib['price'] + 1
  	Prices(child)
Price = {"red": 0, "green": 0, "blue": 0}
root = ElementTree.fromstring(input())
root.attrib['price'] = 1
Prices(root)
for color in Price.keys():
  print(Price[color],end=' ')