with open('C:\\Users\\admin\\Downloads\\dataset_24465_4.txt', 'r') as f:
  Lst = []
  for line in f:
  	Lst.append(line.rstrip())
with open('C:\\Users\\admin\\Downloads\\dataset1.txt', 'w') as f:
  contents = '\n'.join(Lst[::-1])
  f.write(contents)