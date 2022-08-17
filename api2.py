import requests
import json

client_id = '1eb649744aaabdedeed8'
client_secret = '886dc091519ebc328f6b9a27f5ccceee'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
lst = []
with open('C:\\Users\\admin\\Downloads\\dataset_24476_4.txt', 'r') as f1:
  for line in f1:
  	d = json.loads(requests.get("https://api.artsy.net/api/artists/" + line.strip(), headers=headers).text)
  	lst.append(d['birthday'] + ' ' + d['sortable_name'])
lst.sort()
for elem in lst:
  print(elem[5:])