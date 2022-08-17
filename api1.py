import json
import requests
lst = []
with open('C:\\Users\\admin\\Downloads\\dataset_24476_3.txt', 'r') as f1:
  for line in f1:
  	d = json.loads(requests.get('http://numbersapi.com/' + line.strip() + '/math?json').text)
  	lst.append(d['found'])
with open('C:\\Users\\admin\\Downloads\\dataset.txt', 'w') as f2:
  for elem in lst:
    if elem:
      f2.write('Interesting\n')
    else:
      f2.write('Boring\n')