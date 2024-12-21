from bs4 import BeautifulSoup
import requests
url = "https://base.garant.ru/10180094/"
class_ = "content"
r = requests.get(url)
html = BeautifulSoup (r.text)
t = html.find(class_=class_).text
print(t)