from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

URL = 'http://lib.ru/STILMARK/stilmark1.txt' 
resp = urlopen(URL)
html = resp.read()
soup = BeautifulSoup(html, 'html.parser')

pattern = r"[^а-яА-Я \t\n\r\f\v]"
Text = re.sub(pattern, '', soup.find('pre').text)

Our_string = ''.join([word[:1] for word in Text.split()])
print(Our_string)
