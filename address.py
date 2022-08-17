import requests
c = 0
with open('F:\\dataset_3378_2.txt','r') as f:
  line = f.readline()
r = requests.get(line.strip())
r = r.text.splitlines()
for l in r:
  c += 1
print(c)