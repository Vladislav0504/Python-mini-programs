import simplecrypt
with open('C:\\Users\\admin\\Downloads\\encrypted.bin', 'rb') as inp:
  encrypted = inp.read()
with open('C:\\Users\\admin\\Downloads\\passwords.txt', 'r') as f:
  for line in f:
    password = line.strip()
    try:
      print(simplecrypt.decrypt(password, encrypted).decode('utf8'))
    except simplecrypt.DecryptionException:
      print(password, 'is wrong')
    else:
      print(password, 'is correct')