import os.path
Lst = []
for current_dir, dirs, files in os.walk('C:\\Users\\admin\\Downloads\\main'):
  for elem in files:
  	if elem.endswith('.py'):
  	  Lst.append(current_dir[25:])
  	  break
Lst.sort()
contents = '\n'.join(Lst)
with open('C:\\Users\\admin\\Downloads\\dataset.txt','w') as f:
  f.write(contents)
