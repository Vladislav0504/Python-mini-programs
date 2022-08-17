import requests
url = ''
with open('F:\\dataset_3378_3.txt','r') as f:
  line = f.readline()
  sp = [j for j in line.split('/')]
  url = sp[0] + '//'
  for i in range(2,len(sp)-1):
  	url = url + sp[i] + '/' 
  r = requests.get(line.strip())
  r = r.text.splitlines()
c = '12'
while c != 'We':
	for l in r:
		if (l[0] != 'W') and (l[1] != 'e'):
			r = requests.get((url + l).strip())
			r = r.text.splitlines()
			c = l[0] + l[1]
			break
		else:
			c = l[0] + l[1]
			break
c = ''
for l in r:
	c = c + l + '\n'
with open('F:\\text.txt','w') as f1:
  f1.write(c)