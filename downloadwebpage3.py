from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html').read().decode('utf-8') # считываем содержимое
s = str(html)
soup = BeautifulSoup(s, 'html.parser')
summ = 0
for td in soup.find_all('td'):
  summ += int(td.renderContents())
print(summ)
	